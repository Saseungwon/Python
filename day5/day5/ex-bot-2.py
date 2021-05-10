#-*- coding: utf-8 -*-
# 텔레그램 챗봇
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd
import requests
import json

APIKEY = '1601770966:AAG_M12JkBrT0CXnLiCK62bVDW4QzNMjKz4'

# updater
updater = Updater(token=APIKEY, use_context=True)
def fn_getCoin(text):
    df = pd.read_excel('altCoin.xlsx', sheet_name='Sheet1', engine='openpyxl')
    print(df.head())
    res = df[df['korean_name'].str.contains(text)]
    codeList = res['market'].values.tolist()
    url = 'https://api.upbit.com/v1/ticker?markets='
    coinInfo_code = []
    coinInfo_price = []
    for i in codeList:
        resp = requests.get(url + i)
        text = resp.text
        json_data = json.loads(text)
        coinInfo_code.append(json_data[0]['market'])
        coinInfo_price.append(json_data[0]['trade_price'])
    return coinInfo_code, coinInfo_price

# message handler
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    print(user_text)
    coinCode, coinPrice = fn_getCoin(user_text)
    for i, v in enumerate(coinCode):
        text = "코드 : " + coinCode[i] + ', 현재 가격 : ' + str(coinPrice[i])
        context.bot.send_message(chat_id=user_id, text=text)

echo_handler = MessageHandler(Filters.text &(~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)
updater.start_polling()
updater.idle()