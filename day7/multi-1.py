from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('data/datasets-master/streeteasy/manhattan.csv')
print(df.head())
x = df[['bedrooms', 'bathrooms', 'size_sqft',
        'min_to_subway', 'floor', 'building_age_yrs',
        'no_fee', 'has_roofdeck', 'has_washer_dryer',
        'has_dorrman', 'has_elevator', 'has_dishwasher',
        'has_patio', 'has_gym']]
y = df['rent']
# 학습데이터와 교육데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

from sklearn.linear_model import LinearRegression

ml = LinearRegression()
ml.fit(x_train, y_train)

y_predict = ml.predict(x_test)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel('Actual Rent')
plt.ylabel('Prediced Rent')
plt.title('multiple linear regression')
plt.show()

# 기울기
print(ml.coef_)
# y절편
print(ml.intercept_)

print(ml.score(x_train, y_train))