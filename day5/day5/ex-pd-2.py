# -*- coding:utf-8 -*-
import pandas as pd
# Series 자료구조 dataframe 의 한 열은 Series
s = pd.Series([1,2,3])
print(s)
print(s * 2)
df_w_age = pd.DataFrame({"name":["tom", "Tyrell", "Claire"]
                         ,"age" : [60, 25, 33]})
df_w_height = pd.DataFrame({"name":["tom", "Tyrell", "Claire"]
                         ,"height" : [6.2, 4.0, 5.5]})
joined = df_w_age.set_index('name').join(df_w_height.set_index('name'))
print(joined)

#groupby
df = pd.DataFrame({"name":["tom", "Tyrell", "Claire"]
                         ,"height" :[6.2, 4.0, 5.5]
                         ,"gender" :["M","M","F"]})
print(df.groupby("gender").mean())


# 0    1
# 1    2
# 2    3
# dtype: int64
# 0    2
# 1    4
# 2    6
# dtype: int64
#         age  height
# name
# tom      60     6.2
# Tyrell   25     4.0
# Claire   33     5.5
#         height
# gender
# F          5.5
# M          5.1