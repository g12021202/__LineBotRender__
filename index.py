from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['RnWvSM/UJLn8T8IeK9qqsF1Do+XoVkZln4zGpYkJffupMgR4jhX7hTlkW7c5KJb3xcT7ov5iWAE534sDzqWhC4WRVZKv7OGV7gu2SxLhcEGUzjFTXybs0myUltNeQtEwyQh1HRq/dn9/BRH0sIFIHQdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['121c89895cb4eb482567eda1447a4e00'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)