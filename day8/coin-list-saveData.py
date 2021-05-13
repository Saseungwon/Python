# https://api.upbit.com/v1/market/all
# pip install xlsxwriter
import requests
import json
from pandas import json_normalize
import pandas as pd
# 업비트 시세조회 REST API
url ='https://api.upbit.com/v1/market/all'
resp = requests.get(url)
text = resp.text
json_data = json.loads(text)
# print(json_data)
# print(json_data[0].get("market"))

# pandas dataframe 형태로
df = json_normalize(json_data)
print(df)
## XlsxWriter 엔진으로 Pandas writer 객체 만들기
writer = pd.ExcelWriter('AlternativeCoin_List.xlsx', engine='xlsxwriter')
## DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name='Sheet1')
## Pandas writer 객체 닫기
writer.close()
