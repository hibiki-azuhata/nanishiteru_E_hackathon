from flask import Flask
from flask import request
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
import flex

# generate instance
app = Flask(__name__)

# get environmental value from heroku
ACCESS_TOKEN = "TOKEN"
CHANNEL_SECRET = "TOKEN"
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# endpoint
@app.route("/")
def test():
    return "<h1>It Works!</h1>"


# endpoint from linebot
@app.route("/callback", methods=['POST'])
def callback():
    print("callbackは")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        # abort(400)
    return 'OK'


# handle message from LINE
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("なんかきたで")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


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
                text = event["message"]["text"]
                user_id = event["source"]["userId"]
                reply_token = event["replyToken"]

                # テキストメッセージの内容を使って適切な応答を生成する処理を実装
                flex.response()
    # 200 OKを返す
    return "OK"


if __name__ == "__main__":
    app.run()
