import requests
import json

WORK_URL = "URL"
WORK_TOKEN = "TOKEN"
BROWSE_URL = "URL"
BROWSE_TOKEN = "TOKEN"
ACC_TOKEN_URL = "URL"
ACC_TOKEN_TOKEN = "TOKEN"


def get_kintone(url, api_token):
    """kintoneのレコードを1件取得する関数"""
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(url, headers=headers)
    a = resp.json()
    return a

def get_worktable(uuid):
    work_table = get_kintone(f'https://t8a1k4j7wzii.cybozu.com/k/v1/records.json?app=3&query=uuid="{uuid}"', WORK_TOKEN)
    
    return work_table["records"]

def get_browsetable(uuid):
    browse_table = get_kintone(f'https://t8a1k4j7wzii.cybozu.com/k/v1/records.json?app=4&query=uuid="{uuid}"', WORK_TOKEN)

    return browse_table["records"]

# 個人識別テーブルにレコードを登録
def add_tokentable(body):
    headers = {
        "X-Cybozu-API-Token" : ACC_TOKEN_TOKEN,
         "Content-Type": "application/json"
    }
    requests.post("https://t8a1k4j7wzii.cybozu.com/k/v1/record.json", headers=headers, json=body)

# 個人識別テーブルから全レコードを取得
def get_tokentable():
    headers = {"X-Cybozu-API-Token" : ACC_TOKEN_TOKEN}
    resp = requests.get(ACC_TOKEN_URL, headers=headers)

    return resp.json()["records"]

# 個人識別テーブルの、一致するレコードIDのレコードを削除
def delete_person(record_id):
    headers = {"X-Cybozu-API-Token" : ACC_TOKEN_TOKEN}
    resp = requests.delete(f"{ACC_TOKEN_URL}&ids[0]={record_id}", headers=headers)

    return resp

if __name__ == "__main__":
    print(get_worktable("185410946378514"))
