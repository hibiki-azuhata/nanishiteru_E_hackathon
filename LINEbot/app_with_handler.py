# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

flexcontent = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "山田太郎",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "忙しさ"
          },
          {
            "type": "text",
            "text": "70%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "70%",
                "backgroundColor": "#0D8186",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "Google chrome"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "30"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "鈴木二郎",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "忙しさ"
          },
          {
            "type": "text",
            "text": "30%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "30%",
                "backgroundColor": "#DE5658",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF6B6E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "vscode"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "20"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "高橋三郎",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "忙しさ"
          },
          {
            "type": "text",
            "text": "100%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "100%",
                "backgroundColor": "#7D51E4",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#A17DF5",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "Slack"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "5"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    }
  ]
}

flexcontent1 = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "酒井",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "悩み度"
          },
          {
            "type": "text",
            "text": "12%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "12%",
                "backgroundColor": "#0D8186",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "IntellijIDEA"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "12"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "篠崎",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "悩み度"
          },
          {
            "type": "text",
            "text": "83%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "83%",
                "backgroundColor": "#DE5658",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF6B6E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "FireFox"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "68"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "小豆畑",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "悩み度"
          },
          {
            "type": "text",
            "text": "42%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "42%",
                "backgroundColor": "#7D51E4",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#A17DF5",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Active window",
                "color": "#8C8C8C",
                "size": "sm",
              }
            ],
            "flex": 1
          },
          {
            "type": "text",
            "text": "PyCharm"
          },
          {
            "type": "text",
            "text": "タイプ数",
            "color": "#8C8C8C",
            "size": "sm",
          },
          {
            "type": "text",
            "text": "55"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
        }
      }
    }
  ]
}


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    if event.message.text == "先輩の忙しさを確認！":
        flex_message = FlexSendMessage(
        alt_text='hello',
        contents=flexcontent
        )
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )
    elif event.message.text == "新人の悩み度を確認！":
        flex_message = FlexSendMessage(
        alt_text='hello',
        contents=flexcontent1
        )
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )    


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
