# -*- coding: utf-8 -*-
"""InClass_DL_Lab_Sales_Prediction.ipynb

Automatically generated by Colab.


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('salespredict.csv')

df.describe()

import tensorflow as tf
print(tf.__version__)

model.compile(optimizer =tf.keras.optimizers.Adam(),
              loss = 'sparse_catgeorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)


