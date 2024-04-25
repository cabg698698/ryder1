from flask import Flask
from linebot import LineBotApi, WebhookHandler
import configparser


app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

#TODO:LINE聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot','channel_access_token'))
handler = WebhookHandler(config.get('line-bot','channel_secret'))

#TODO:最後再把分散各地的程式碼呼叫進來
from app import routes,models_for_line