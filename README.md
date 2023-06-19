# nanishiteru_E_hackathon
6/17,18 BIPROGYハッカソン Eチーム成果物

## 作品名「何してる？」

### 概要
各エンジニアの「忙しさ」、「悩み度」をLINE上で閲覧できるツールです。
「忙しさ」「悩み度」は、あるウィンドウをどれぐらいの時間アクティブにし、どれだけタイピングしているかを元に自動で計算されます。

### システム構成
![image](https://github.com/hibiki-azuhata/nanishiteru_E_hackathon/assets/106302513/a1df2919-1c23-49ae-94d1-84983d0e38e4)

#### ./LINEbot
図中LINE Botに該当します。
#### ./busy-trouble-checker
図中バックグラウンドサービスに該当します。
#### ./hackathon
図中APIサーバに該当します。
#### ./liff-user-api
図中LINE認証サーバに該当します。
