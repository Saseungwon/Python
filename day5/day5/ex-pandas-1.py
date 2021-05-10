import  pandas as pd
# 데이터프레임 : 자료구조 데이터 프레임은 SQL 테이블 형태
# 행과 열로 이루어진 표 형식

df = pd.DataFrame({"name":["Bob", "Alex", "Jenice"]
                   ,"age": [60, 25, 33]})

# index
print(df.index)
print(df.head())
print(df['age'])
df['age_plus_one'] = df['age'] + 1
df['age_two'] = df['age'] + 2
df['age_squared'] = df['age'] *df['age']
df['over_30'] = df['age'] > 30
print(df.head())
# 함수 이용가능
total_sum = df['age'].sum()
df['age_squared2'] = df['age'].apply(lambda x : x * x)


    # RangeIndex(start=0, stop=3, step=1)
    #      name  age
    # 0     Bob   60
    # 1    Alex   25
    # 2  Jenice   33
    # 0    60
    # 1    25
    # 2    33
    # Name: age, dtype: int64
    #      name  age  age_plus_one  age_two  age_squared  over_30
    # 0     Bob   60            61       62         3600     True
    # 1    Alex   25            26       27          625    False
    # 2  Jenice   33            34       35         1089     True
    #
    # Process finished with exit code 0
