# https://api.upbit.com/v1/market/all
import requests
import json
from pandas import json_normalize
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
