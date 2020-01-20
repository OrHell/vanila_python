# Импорт необходимых для работы библиотек
import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Чтение данных из дата сета
data_file=pd.read_csv('parkinsons.data')
data_file.head()
# Получение всех значений стобца "status"
features=data_file.loc[:,data_file.columns!='status'].values[:,1:]
labels=data_file.loc[:,'status'].values
# На данном этапе имеется 147 единиц означающих статус "болен" и 48 нулей - статус здоров 

# Масштабирование объектов от -1 до 1, чтобы нормализовать их
scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features) # Данный метод подгоняет данные и затем преобразует их
y=labels # Эти данные не нужно масштабировать
# Деление набора данных на обучение и тестирование, данные для тестирования "test_size" 20%
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=7) 
model_data=XGBClassifier()
# Используя алгоритм повышения градиента (XGB), который обучает и прогнозиует
# несколько моделей для получения превосходного результата
model_data.fit(x_train,y_train)
y_pred=model_data.predict(x_test)

pred_mode = accuracy_score(y_test, y_pred)*100 # Генерация прогнозируемого значения и точность модели

print("Процент Статуса болезни (Здоров)",pred_mode)
print("Процент Статуса болезни (Болен)",100-pred_mode)
