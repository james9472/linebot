import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    #reply_basic = TextSendMessage(text=f"{get_message}")
    reply_basic=event.message.text
    if reply_basic == 'A': 
        reply = ImageSendMessage(
    original_content_url='https://ppt.cc/ffOxsx@.jpg',
    preview_image_url='https://ppt.cc/ffOxsx@.jpg'
)
      #  reply = ImageSendMessage(original_content_url='https://ppt.cc/ffOxsx@.jpg',preview_image_url='https://ppt.cc/ffOxsx@.jpg')
     #   line_bot_api.reply_message(event.reply_token,reply)
       # reply = TextSendMessage(text=f"A10")
    elif reply_basic == 'B': 
        reply = TextSendMessage(text=f"B10")
    elif reply_basic == 'C': 
        reply = TextSendMessage(text=f"C10")
    elif reply_basic == 'D': 
        reply = TextSendMessage(text=f"D10")
       
    #reply = TextSendMessage(text=f"hello")
    #reply = 'here'
    line_bot_api.reply_message(event.reply_token, reply)
    #line_bot_api.reply_message(event.reply_token,reply)
    #ine_bot_api.reply_message('here')
