#http://api.upbit.com/markey/all

import requests
import json
from pandas import json_normalize
import pandas as pd

url = 'https://api.upbit.com/v1/market/all'
resp = requests.get(url)
text = resp.text
json_data = json.loads(text)
print(json_data)
df = json_normalize(json_data)

#pandas excel 생성
#pip install xlsxwriter
writer = pd.ExcelWriter('altCoin.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.close()