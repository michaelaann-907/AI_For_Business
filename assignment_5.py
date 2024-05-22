# -*- coding: utf-8 -*-
"""Assignment_5.ipynb

Automatically generated by Colab.


Predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable.

Target Variable (trying to predict) = SalePrice
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df_train=pd.read_csv('train.csv')
df_test=pd.read_csv('test.csv')

df_train.head()

df_test.head()

df_train.columns

df_test.columns

df_train.describe()

df_train.shape

df_test.shape

# Calculate # of missing values (NaN or null values) in each column of a df
df_train.isnull().sum()

df_train.SalePrice.describe()

target = np.log(df_train.SalePrice)
print(target.skew())
plt.hist(target, color='purple')
plt.show()

data = df_train.select_dtypes(include=[np.number]).interpolate().dropna()

# check to see if all columns have 0 null values
sum(data.isnull().sum() != 0)

# preparing linear model
# assign features to X, SalePrice to Y
y = np.log(df_train.SalePrice)
X = data.drop(['SalePrice', 'Id'], axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                          X, y, random_state=42, test_size=.33)

# Create model

from sklearn import linear_model

lr = linear_model.LinearRegression()

# Fit the model
model = lr.fit(X_train, y_train)

print ("R^2 is: \n", model.score(X_test, y_test))

prediction = model.predict(X_test)

from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, prediction))

values = y_test
plt.scatter(prediction, values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('Linear Regression Model')
plt.show()

sublesson = pd.DataFrame()
sublesson['Id']=df_test.Id

features = df_test.select_dtypes(
          include=[np.number]).drop(['Id'], axis=1).interpolate()

prediction = model.predict(features)

final_prediction = np.exp(prediction)

print ("Original predictions are: \n", prediction[:5], "\n")
print ("Final predictions are: \n", final_prediction[:5])

sublesson['SalePrice'] = final_prediction
sublesson.head()

sublesson.to_csv('predictions.csv', index=False)