import pandas as pd

# 데이터프레임
# 팬더스는 데이터 프레임을 기본으로 돌아감, 데이터프레임은 SQL 테이블 또는 R의 데이터프레임과 비슷
# 행과 열로 이루어진 표
# 데이터프레임을 활용하면 각 열에 있는 값에 여러 연산을 편하게 적용할 수 있음

df = pd.DataFrame({"name": ["Bob","Alex","Janice"],
                   "age":[60,25,33]})
# 데이터프레임을 사용할 때는 색인(index)에 유의합니다. 행마다 색인을 하나씩 가지고 있고 보통 행번호를 색인 값으로 사용
# print(df.index)
print(df['name'].shape)
# csv 파일에서 데이터브레임을 만들 수 있다.
# other_df = pd.read_csv("myfile.csv")

# 기존 열을 이용해 새로운 열을 쉽게 만들 수 있다
df["agd_plus_one"] = df["age"] + 1
df["age_times_two"] = 2 * df["age"]
df["age_squared"] = df["age"] * df["age"]
df["over_30"] = (df["age"] > 30)
# 데이터프레임의 열에도 내장 함수가 있음.
total_age = df["age"].sum() # 합을 구함
median_age = df["age"].quantile(0.5)
# print(df)
# print(total_age)
# print(median_age)


# 데이터 프레임에서 여러 행을 불러오고 다시 새로운 데이터 프레임을 만들 수 있음
df_below50 = df[df["age"] < 50]
# print(df_below50)

#  람다함수 (일시적으로 쓰고버리는 함수
f = lambda x, y : x + y
# print(f(4,4))
# 열에 람다 함수를 적용할 수 있다
df["age_squared"] = df["age"].apply(lambda x: x * x)
# print(df)





