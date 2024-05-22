# -*- coding: utf-8 -*-
"""InClassLab_CreditCardFraudTransactionDetection.ipynb

Automatically generated by Colab.


"""

import pandas as pd
df = pd.read_csv('creditcard.csv')
df

df['Class'].value_counts()

df.hist(bins=30, figsize=(30,30))

df.describe()

df.isnull().sum()

df.dropna(inplace=True)

from sklearn.preprocessing import RobustScaler
new_df = df.copy()
new_df['Amount'] = RobustScaler().fit_transform(new_df['Amount'].to_numpy().reshape(-1,1))
time = new_df['Time']
new_df['Time'] = (time - time.min()) / (time.max() - time.min())
new_df

new_df = new_df.sample(frac=1, random_state=1)
new_df

train, test, val = new_df[:240000], new_df[240000:262000], new_df[262000:]
train['Class'].value_counts(), test['Class'].value_counts(), val['Class'].value_counts()

train_np, test_np, val_np = train.to_numpy(), test.to_numpy(), val.to_numpy()
train_np.shape, test_np.shape, val_np.shape

x_train, y_train = train_np[:, :-1], train_np[:,-1]
x_test, y_test = test_np[:, :-1], test_np[:, -1]
x_val, y_val = val_np[:, :-1], val_np[:, -1]
x_train.shape, y_train.shape, x_test.shape, y_test.shape, x_val.shape, y_val.shape

y_train

x_train

from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(x_train, y_train)
logistic_model.score(x_train, y_train)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(y_val, logistic_model.predict(x_val))

from sklearn.ensemble import RandomForestClassifier
rf= RandomForestClassifier(max_depth=2, n_jobs=-1)
rf.fit(x_train, y_train)
ConfusionMatrixDisplay.from_predictions(y_val, rf.predict(x_val))

from tensorflow import keras
from keras.layers import Dense, InputLayer, BatchNormalization
from keras.models import Sequential, load_model
from keras.callbacks import ModelCheckpoint

shallow_nn = Sequential()
shallow_nn.add(InputLayer((x_train.shape[1],)))
shallow_nn.add(Dense(2, 'relu'))
shallow_nn.add(BatchNormalization())
shallow_nn.add(Dense(1, 'sigmoid'))

checkpoint = ModelCheckpoint('shallow_nn', save_best_only=True)
shallow_nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

shallow_nn.summary()

shallow_nn.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=5, callbacks=checkpoint)

def neural_net_predictions(model, x):
  return(model.predict(x).flatten() > 0.5).astype(int)
neural_net_predictions(shallow_nn, x_val)

ConfusionMatrixDisplay.from_predictions(y_val, neural_net_predictions(shallow_nn, x_val))