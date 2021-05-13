import pandas as pd
# Series 자료구조
# 데이터 프레임의 열이 시리즈임. (파이선 리스트와 달리 동일한 자료형으로 이루어짐)

s = pd.Series([1,2,3])
print(s)                     # 인덱스와 값
print(s +2)                  # 전체에 2더함
print(s.index)               # s 인덱스
print(s + pd.Series([4,4,5])) # 길이가 같은 두 시리즈를 더하면 성분별로 덧셈을 함.

# 데이터 프레임의 병합 또는 분할 ( sql join, grouping)

df_w_age = pd.DataFrame({
                          "name" : ["Tom","Tyrell","Claire"],
                          "age" : [60, 25, 33]
})
df_w_height = pd.DataFrame({
                            "name": ["Tom","Tyrell", "Claire"],
                            "height": [6.2, 4.0, 5.5]
})
joined = df_w_age.set_index("name").join(df_w_height.set_index("name"))
print(joined)
print(joined.reset_index())

df = pd.DataFrame({"name" : ["Tom", "Tyrell","Claire"],
                   "age" : [60, 25, 33],
                   "height" : [6.2, 4.0, 5.5],
                   "gender" : ["M","M","F"]
})

print(df.groupby("gender").mean())

# medians = df.groupby("gender").quantile(0.5)

def agg(ddf):
    return pd.Series({
        "name": max(ddf["name"]),
        "oldest" : max(ddf["age"]),
        "mean_height":ddf["height"].mean()
    })
print(df.groupby("gender").apply(agg))

