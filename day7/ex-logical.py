import pandas as pd

passengers = pd.read_csv('data/dataset/Titanic Passengers.csv')
print(passengers)

# 사망 0 생존 1
# 남자 0 여자 1
passengers['sex'] = passengers['sex'].map({'male':0, 'female':1})
passengers['age'].fillna(value=passengers['age'].mean(), inplace=True)
features = passengers[['sex', 'age', 'pclass']]
survival = passengers['survived']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(features, survival)

from sklearn.preprocessing import StandardScaler

# 스케일 조정
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
print(model.score(x_train, y_train))

# 테스트
import numpy as np

Jack = np.array([0.0, 20.0, 3.0])
Rose = np.array([1.0, 17.0, 1.0])
Nick = np.array([1.0, 27.0, 1.0])
sample_pass = np.array([Jack, Rose, Nick])
sample_pass = scaler.fit_transform(sample_pass)
print(model.predict(sample_pass))