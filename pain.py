import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_file=pd.read_csv('parkinsons.data')
data_file.head()

features=data_file.loc[:,data_file.columns!='status'].values[:,1:]
labels=data_file.loc[:,'status'].values

scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=7)
model_data=XGBClassifier()

model_data.fit(x_train,y_train)
y_pred=model_data.predict(x_test)

pred_mode = accuracy_score(y_test, y_pred)*100

print("Процент Статуса болезни (Здоров)",accuracy_score(y_test, y_pred)*100)
print("Процент Статуса болезни (Болен)",100-(accuracy_score(y_test, y_pred)*100))
