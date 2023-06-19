"""
YOUR_CHANNEL_ACCESS_TOKENを実際のチャネルアクセストークンに置き換えてください。
USER_IDはメッセージを送信するユーザーのIDに置き換えてください。
"""
import requests

# Flex Messageのコンテンツを定義する
flexcontent2 = {
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
            "text": "エンジニアA",
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
            "text": "エンジニアB",
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
            "text": "エンジニアC",
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

# Flex Messageオブジェクトを作成する
flex_message = {
    "type": "flex",
    "altText": "This is a Flex Message",
    "contents": flexcontent2
}

# Messaging APIにFlex Messageを送信する
channel_access_token = "JZghVl47RBuGhyCY6z3X1a+HDgOOkZJcQh+grtamcbvhPouJkgvcrARqjH6g3rmeQSj3QKuGz+gm2gSjcQCtM7E5NNSR/aZWaFRH6jo/HFMjxomcFrYFl8z6JUgc8FNvjIARzQbE0Q1CvamSJvTMTQdB04t89/1O/w1cDnyilFU="
line_api_url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {channel_access_token}"
}

data = {
    "to": "U518ed73743ceb8f81e928224b21251a6",
    "messages": [flex_message]
}


def response():
    response = requests.post(line_api_url, headers=headers, json=data)
    print(response.status_code, response.text)

if __name__ == "__main__":
    response()
