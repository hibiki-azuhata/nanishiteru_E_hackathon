import time
import webbrowser

import psutil
import win32api
import win32gui
import win32process
from pynput import keyboard, mouse


def get_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


def get_window():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        exe_name = psutil.Process(pid[-1]).name()
        path = psutil.Process(pid[-1]).exe()
        lang, codepage = win32api.GetFileVersionInfo(path, '\\VarFileInfo\\Translation')[0]
        file_desc = win32api.GetFileVersionInfo(path, u"\\StringFileInfo\\%04x%04x\\%s" % (lang, codepage, "FileDescription"))
        return file_desc if len(file_desc) > 0 else exe_name
    except Exception:
        return ""


class Service:
    def __init__(self):
        self.browser = get_window()
        print(self.browser)

        self.data = []

    def update_data(self, window, is_click):
        if self.data[-1].window != window:
            self.data[-1].switch()
            self.data += [ActiveData(window, get_title(), 0 if is_click else 1)]
        elif not is_click:
            self.data[-1].update()

    def trigger(self, is_click):
        self.update_data(get_window(), is_click)

    def reset(self):
        self.data = [ActiveData(get_window(), get_title(), 0)]

    def get_data(self):
        if len(self.data) > 0:
            self.data[-1].switch()
        return list(map(lambda d: d.to_dict(), self.data))

    def run(self):
        self.data += [ActiveData(get_window(), get_title(), 0)]
        keyboard_listener = keyboard.Listener(on_press=lambda key: self.trigger(False))
        mouse_listener = mouse.Listener(on_click=lambda x, y, btn, pressed: self.trigger(True))
        keyboard_listener.start()
        mouse_listener.start()


class ActiveData:
    def __init__(self, window, title, types):
        self.window = window
        self.title = title
        self.types = types
        self.start = time.time()
        self.during = None

    def update(self):
        self.types += 1

    def switch(self):
        self.during = int(time.time() - self.start)

    def get_during(self):
        if self.during is None:
            self.switch()
        return int(self.during)

    def to_dict(self):
        return {"window_name": self.window, "window_title": self.title, "num_of_types": self.types, "utilization_time": self.during}

