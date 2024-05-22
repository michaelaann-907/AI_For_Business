# -*- coding: utf-8 -*-
"""CodeAlong12_Titanic.ipynb

Automatically generated by Colab.


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

train_data=pd.read_csv('train.csv')
test_data=pd.read_csv('test.csv')
test_ids=test_data['PassengerId']

train_data.info()

"""The attributes have the following meaning:

PassengerId: a unique identifier for each passenger
Survived: that's the target, 0 means the passenger did not survive, while 1 means he/she survived.
Pclass: passenger class.
Name, Sex, Age: self-explanatory
SibSp: how many siblings & spouses of the passenger aboard the Titanic.
Parch: how many children & parents of the passenger aboard the Titanic.
Ticket: ticket id
Fare: price paid (in pounds)
Cabin: passenger's cabin number
Embarked: where the passenger embarked the Titanic

"""

test_data.info()

train_data.head()

def clean(data):
  data=data.drop(['Ticket', 'Name', 'PassengerId', 'Cabin'], axis=1)

  cols=['Age', 'SibSp', 'Parch', 'Fare']
  for col in cols:
    data[col].fillna(data[col].median(), inplace=True)

  data.Embarked.fillna('U', inplace=True)
  return data


train_data=clean(train_data)
test_data=clean(test_data)

train_data.info()

test_data.info()

from sklearn import preprocessing
le=preprocessing.LabelEncoder()

columns=['Sex', 'Embarked']

for col in columns:
  train_data[col]=le.fit_transform(train_data[col])
  test_data[col]=le.fit_transform(test_data[col])

train_data.head(10)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X=train_data.drop('Survived', axis=1)
y=train_data['Survived']

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=55)

model_lr=LogisticRegression(random_state=0, max_iter=1000).fit(X_train,y_train)

predictions=model_lr.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

submission_preds=model_lr.predict(test_data)

df=pd.DataFrame({"PassengerId": test_ids.values,
                 "Survived": submission_preds})

df.to_csv("submission.csv", index=False)



import numpy as np

# Assuming 'data' is your NumPy array
shape = y_train.shape
print("Shape of data:", shape)

# APPLY DEEP LEARNING

!pip install tensorflow

import tensorflow as tf

from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

model =Sequential()

model.add(Dense(10, activation='relu')),
model.add(Dense(16, activation='relu')),
model.add(Dense(8, activation='relu')),
model.add(Dense(4, activation='relu')),
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics='accuracy')

# fit the model
model.fit(X_train,y_train, validation_data=(X_test,y_test), epochs=15, batch_size=10)

# evaluate
model.evaluate(X_test,y_test)

#Compile model
model.compile(optimizer='adam', loss='mean_absolute_error')

#train model
model.fit(X_train, y_train, epochs=50)

#evaluate model
test_loss=model.evaluate(X_test,y_test)