import pandas as pd
import requests
import json
#APIKEY = '1601770966:AAG_M12JkBrT0CXnLiCK62bVDW4QzNMjKz4'
def fn_getCoin(text):
    df = pd.read_excel('./altCoin.xlsx', sheet_name='Sheet1', engine='openpyxl')
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

a, b = fn_getCoin('도지코인')
print(a)
print(b)