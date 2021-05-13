# https://api.upbit.com/v1/market/all
# pip install xlrd
# pip install openpyxl

import pandas as pd

def fn_search_coin(text):
    df = pd.read_excel('./AlternativeCoin_List.xlsx', sheet_name='Sheet1',  engine='openpyxl')
    # 특정 명칭
    res = df[df['korean_name'].str.contains(text)]
    codeList = res['market'].values.tolist()
    nameList = res['korean_name'].values.tolist()
    return codeList, nameList
codeList, nameList = fn_search_coin('비트')

