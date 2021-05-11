import pandas as pd
from sklearn.linear_model import  LinearRegression
df = pd.read_csv('heights.csv')
x = df('height')
y = df('weight')

line_filter = LinearRegression()
data = x.values.reshape(-1, 1)
line_filter.fit(data, y)

print(line_filter.predict([70]))
print(line_filter.coef_) # 기울기 a, w
print(line_filter.intercept_) # y절편 b

import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.plot(x, line_filter.predict(data))
plt.show()