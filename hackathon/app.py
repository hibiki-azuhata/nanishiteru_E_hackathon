from flask import Flask, request
from flask_cors import CORS
import json
from kintone import *
from weight import *
import time

app = Flask(__name__)
CORS(app)

@app.route("/dummy")
def get_status():
    data = [
            {
                "line_id" : 0,
                "role" : 0,
                "active_window" : "Microsoft Teams",
                "type_count" : 0,
                "status_value" : 70,
                "content" : ""
            },
            {
                "line_id" : 1,
                "role" : 0,
                "active_window" : "Visual Studio Code",
                "type_count" : 450,
                "status_value" : 80,
                "content" : ""
            },
            {
                "line_id" : 2,
                "role" : 1,
                "active_window" : "Visual Studio Code",
                "type_count" : 500,
                "status_value" : 10,
                "content" : ""
            },
            {
                "line_id" : 3,
                "role" : 1,
                "active_window" : "Google Chrome",
                "type_count" : 200,
                "status_value" : 80,
                "content" : "kintoneのAPI呼び出しをどうすればいいかがわかりません"
            },
        ]

    return json.dumps(data)

@app.route("/")
def test():
    data = []

    token_table = get_tokentable()
    print(token_table[1])

    for person in token_table:        
        uuid = person["uuid"]["value"]
        token = person["token"]["value"]

        print(person)
        print(uuid, token)

        if float(person["expired_time"]["value"]) > time.time():
            print("expire")
            delete_person(person["レコード番号"]["value"])
            continue

        work_info = get_worktable(uuid)
        active_window = ""
        utilization_time = 0
        type_count = 0
        is_busy = False
        for record in work_info:
            if record["window_name"]["value"] == "BUSY_TROUBLE_CHECKER__ENUM__BUSY_NOW":
                is_busy = True
            if float(record["utilization_time"]["value"]) > utilization_time:
                utilization_time = float(record["utilization_time"]["value"])
                active_window = record["window_name"]["value"]
                type_count = int(record["num_of_types"]["value"])
        role = int(work_info[-1]["role"]["value"])

        content = ""
        if role == 0:
            # 先輩
            if type_count < 100:
                status_value = 0
            elif type_count < 500:
                status_value = 1
            else:
                status_value = 2
            if active_window in MEETING or is_busy:
                status_value = 2
        else:
            # 新人
            search_info = get_browsetable(uuid)
            if type_count < 100:
                status_value = 0
            elif type_count < 500:
                status_value = 1
            else:
                status_value = 2
            browse_time = 0
            browse_site = ""
            for record in search_info:
                if float(record["browse_time"]["value"]) > browse_time:
                    browse_time = float(record["browse_time"]["value"])
                    browse_site = record["browse_site"]["value"]
            content = f"最近の閲覧：{browse_site}を{browse_time}分閲覧"
            
        data.append({
            "token" : token,
            "role" : role,
            "active_window" : active_window,
            "type_count" : type_count,
            "status_value" : status_value,
            "content" : content
        })

        return json.dumps(data)
    
@app.route("/add_token", methods=["POST"])
def post():
    body = request.get_data()
    print(body)
    body = json.loads(body.decode("utf-8"))
    print(body)
    add_tokentable(body)
    print(body)
    return body

if __name__ == "__main__":
    app.run()