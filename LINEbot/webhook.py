from flask import Flask, request
import flex

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    # LINE Messaging APIからのリクエストを受信
    data = request.get_json()
    events = data["events"]
    flex.response()

    for event in events:
        # イベントがメッセージイベントかどうかをチェック
        if event["type"] == "message":
            message_type = event["message"]["type"]
            if message_type == "text":
                # ユーザがテキストメッセージを送信した場合の処理
                # text = event["message"]["text"]
                # user_id = event["source"]["userId"]
                # reply_token = event["replyToken"]

                # テキストメッセージの内容を使って適切な応答を生成する処理を実装
                flex.response()
    # 200 OKを返す
    return "OK"


if __name__ == "__main__":
    app.run()
