import json
import time

import webbrowser
from uuid import getnode as get_mac
from pystray import Icon, Menu, MenuItem
from PIL import Image
from plyer import notification
import threading
import schedule
import requests

from config import Config
from service import Service

post_url = "URL"

headers_work = {
  "X-Cybozu-API-Token": "TOKEN",
  "Content-Type": "application/json"
}

headers_searchinfo = {
  "X-Cybozu-API-Token": "TOKEN",
  "Content-Type": "application/json"
}

headers_auth = {
  "X-Cybozu-API-Token": "TOKEN"
}

browsers = [
    "Opera Internet Browser", "Google Chrome", "Firefox", "Microsoft Edge", "Safari"
]

BUSY = "BUSY_TROUBLE_CHECKER__ENUM__BUSY_NOW"


class Tray:
    def __init__(self, config: Config):
        self.service = Service()
        self.config = config
        image = Image.open("icon.jpg")
        self.login()

        self.menu = Menu(
            MenuItem('認証', self.login),
            MenuItem('今忙しいボタン', self.busy_now),
            MenuItem('先輩', self.config.set_senpai, checked=lambda _: self.config.role == 0, radio=True),
            MenuItem('新人', self.config.set_shinjin, checked=lambda _: self.config.role == 1, radio=True),
            MenuItem('終了', self.stop)
        )

        self.icon = Icon(name='busy_trouble_checker', title='何してる？通知', icon=image, menu=self.menu)

    def login(self):
        webbrowser.open(f"URL/?uuid={get_mac()}")

    def logout(self):
        webbrowser.open(f"URL/logout")

    def busy_now(self):
        self.service.update_data(BUSY, False)

    def stop(self):
        self.icon.stop()

    def auth(self, uuid):
        response = requests.get(post_url + f"?app=6", headers=headers_auth)
        for record in response.json()["records"]:
            if uuid == record["uuid"]:
                return True
        return False


    def job(self):
        uuid = get_mac()
        if self.auth(uuid):
            notification.notify(
                title="ログインしてください",
                message="作業情報を送信できませんでした",
                app_name="忙しさ/お悩み確認君",
                app_icon="./alert.ico",
                timeout=10
            )
        record_data = []
        for data in self.service.data:
            record_data += [{
                "send_time": {"value": time.time()},
                "role": {"value": self.config.role},
                "window_name": {"value": data.window},
                "num_of_types": {"value": data.types},
                "utilization_time": {"value": data.get_during()},
                "uuid": {"value": uuid}
            }]
        requests.post(post_url, headers=headers_work, json={"app": 3, "records": record_data})
        trouble_data = []
        for data in self.service.data:
            if data.window in browsers:
                trouble_data += [{
                    "browse_site": {"value": data.title},
                    "browse_time": {"value": data.get_during()},
                    "uuid": {"value": uuid},
                    "send_time": {"value": time.time()}
                }]
        requests.post(post_url, headers=headers_searchinfo, json={"app": 4, "records": trouble_data})
        self.service.reset()

    def scheduler(self):
        schedule.every(5).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def run(self):
        thread_tray = threading.Thread(name="busy_trouble_checker_tray", target=self.scheduler, daemon=True)
        thread_tray.start()
        thread_service = threading.Thread(name="busy_trouble_checker_service", target=self.service.run, daemon=True)
        thread_service.start()

        self.icon.run()


Tray(Config(0, "line")).run()
