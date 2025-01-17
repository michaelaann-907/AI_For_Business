# -*- coding: utf-8 -*-
"""CodeAlong9_Seaborn.ipynb

Automatically generated by Colab.


Seaborn: Statistical Data Visualization
"""

# https://seaborn.pydata.org/index.html

import seaborn as sns

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pwd

"""# df.head()

This method is used to display the first few rows of a DataFrame. By default, it shows the first 5 rows,but you can specify the number of rows you want to display by passing an argument to the method. For example, df.head(10) would display the first 10 rows of the DataFrame df.
"""

df=pd.read_csv('sales.csv')
df.head()

#This method is used to display the first few rows of a DataFrame. By default, it shows the first 5 rows,
#but you can specify the number of rows you want to display by passing an argument to the method.
#For example, df.head(10) would display the first 10 rows of the DataFrame df.

df.tail()
#This method is used to display the last few rows of a DataFrame. Similar to df.head(),
#it also displays 5 rows by default
#but can take an argument to specify the number of rows to display from the end of the DataFrame.

sns.scatterplot(x='Marketing', y='Sales', data=df, hue='Market');

#This code will create a scatter plot with 'Marketing' values on the x-axis
#and 'Sales' values on the y-axis using data from the DataFrame df.

#sns.scatterplot: This is a Seaborn function used to create a scatter plot.
#x='Marketing': This specifies that the 'Marketing' column from the DataFrame df should be used as the values for the x-axis.
#y='Sales': This specifies that the 'Sales' column from the DataFrame df should be used as the values for the y-axis.
#data=df: This specifies that the data for the scatter plot should be taken from the DataFrame df.
#hue='Market': This parameter adds color to the plot based on the values in the 'Market' column. Each unique value in the 'Market' column will be represented by a different color.

plt.savefig('storesales.png')
#saves a figure or plot to a file

plt.figure(figsize=(10,10), dpi=250)

# create a new figure (or plot) with a specified figure size and DPI (dots per inch) resolution.
#figsize=(10, 10): This specifies the size of the figure in inches.
#In this case, the figure will be 10 inches wide and 10 inches tall.
#dpi=250: This specifies the resolution of the figure in dots per inch (DPI). A higher DPI value results in a higher-resolution image when the
#figure is saved to a file using savefig(). In this case, it's set to 250 DPI.


sns.scatterplot(x='Marketing', y='Sales', data=df);

"""Rugplot

A rug plot is a one-dimensional representation of data points along a single axis, typically used to visualize the distribution of a variable.

sns.rugplot: This is a Seaborn function that creates a rug plot.

x='Sales': This specifies that the 'Sales' column from the DataFrame df should be used as the values to be plotted along the x-axis.

data=df: This specifies that the data for the rug plot should be taken from the DataFrame df.
"""

sns.rugplot(x='Sales', data=df)

"""# Displot


sns.displot: This is a Seaborn function that creates a distribution plot, which can be used to visualize the distribution of a single variable.

data=df: This specifies that the data for the distribution plot should be taken from the DataFrame df.

x='Sales': This specifies that the 'Sales' column from the DataFrame df should be used as the variable to be plotted on the x-axis.

bins=20: This parameter specifies the number of bins or intervals into which the data will be divided for the histogram. In this case, it creates 20 bins to group the 'Sales' data.

color='teal': This parameter sets the color of the bars in the histogram to teal.

edgecolor='yellow': This parameter sets the color of the edges of the bars to yellow.

"""

sns.displot(data=df, x='Sales', bins=20, color='teal', edgecolor='yellow');
#create a histogram of the 'Sales' column in the DataFrame df.

"""# KDE

kde=True: This parameter adds a kernel density estimate (KDE) overlay to the histogram. The KDE is a smoothed curve that provides an estimate of the probability density function of the data distribution.

When you execute this code, it will generate a histogram of the 'Sales' data, just like before. However, this time, it will also include a KDE curve overlaid on top of the histogram bars. The KDE curve provides a smoothed representation of the data distribution, allowing you to see the shape of the distribution more clearly and identify potential peaks or modes in the data.
"""

#KDE, kernel density estimate
#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
sns.displot(data=df, x='Sales', bins=20, color='teal', edgecolor='yellow', kde=True);

sns.kdeplot(data=df, x='Sales');
#The KDE plot represents the smoothed probability density of the data, providing insights into the underlying distribution of the 'Sales' variable.
#It can help you visualize the shape of the distribution, identify peaks or modes,
#and get a sense of the data's central tendency and spread.

np.random.seed(25)
# sets the random seed to 25
weekly_sales=np.random.randint(100,150,7)
#This line generates an array of 7 random integers, each between
#100 (inclusive) and 149 (exclusive), using NumPy's randint function.

weekly_sales
#you will see an array of 7 random sales values representing sales for 7 consecutive weeks.
#The values will remain consistent across runs as long as the random seed remains
#the same (i.e., 25).

weekly_sales=pd.DataFrame(weekly_sales, columns=['Sales'])
#creates a pandas DataFrame from the previously generated weekly_sales array and assigns it to the variable weekly_sales.
#It also specifies that the DataFrame should have a single column named 'Sales
weekly_sales

sns.rugplot(data=weekly_sales, x='Sales');
#When you execute this code, it will generate a rug plot of the 'Sales' data.
#In a rug plot, tick marks are placed along a single axis (in this case, the x-axis),
#and each tick mark represents a data point in the 'Sales' column.
#The rug plot helps you visualize the distribution of data points along the axis.

sns.displot(data=weekly_sales, x='Sales', bins=10, kde=True);
#When you execute this code, it will generate a histogram of the 'Sales' data with 10 bins, and it will also overlay a KDE curve on top of the histogram bars. The histogram represents the frequency distribution of sales values,
#while the KDE provides a smoothed, continuous representation of the data's probability density.

#COUNTPLOT
df=pd.read_csv('sales.csv')
df.head()

df['Market'].value_counts()
#This code provides a count of how many times each unique value appears in the 'Market' column and returns the results as a
#pandas Series with the unique values as the index and the counts as the values.

"""plt.figure(figsize=(3, 3), dpi=300): This line of code sets the figure size and DPI (dots per inch) resolution for the upcoming plot created with Matplotlib. The figure will be 3 inches in both width and height, and the DPI will be 300, which results in a high-resolution plot.

sns.countplot(data=df, x='Market'): This line of code uses Seaborn's countplot function to create a bar plot that counts the occurrences of each unique value in the 'Market' column of the DataFrame df. The 'Market' column values are plotted along the x-axis, and the height of each bar represents the count of occurrences of that value.

When you execute this code, it will generate a countplot that displays the distribution of values in the 'Market' column. Each unique market category will have a corresponding bar on the plot, and the height of each bar indicates the number of times that category appears in the 'Market' column.

The plt.figure(figsize=(3, 3), dpi=300) line ensures that the resulting plot has a small physical size (3x3 inches) and a high resolution (300 DPI), which can be useful for saving the plot as an image with high-quality detail.
"""

plt.figure(figsize=(3,3), dpi=300)
sns.countplot(data=df, x='Market');

plt.figure(figsize=(3,3), dpi=300)
sns.countplot(data=df, x='Market', hue='Market Size');

plt.figure(figsize=(3,3), dpi=300)
sns.countplot(data=df, hue='Market', x='Market Size');

"""# Barplot

sns.barplot: This is a Seaborn function used to create a bar plot.

data=df: This specifies that the data for the bar plot should be taken from the DataFrame df.

x='Market Size': This specifies that the 'Market Size' column from the DataFrame df should be used for the values on the x-axis.

y='Sales': This specifies that the 'Sales' column from the DataFrame df should be used for the values on the y-axis.

estimator=np.mean: This parameter specifies the estimator function to compute the height of each bar. In this case, it uses the mean (average) of the 'Sales' values for each 'Market Size' category. So, the height of each bar will represent the average sales for that market size.

errorbar='sd': This parameter specifies that error bars should be added to the bars, and the 'sd' value indicates that the error bars should represent the standard deviation of the 'Sales' values for each 'Market Size' category. Error bars provide a visual representation of the variability or spread of the data.

When you execute this code, it will generate a bar plot with 'Market Size' on the x-axis, 'Sales' on the y-axis, and each bar representing the average sales for a specific market size category. Additionally, error bars will show the standard deviation of sales within each category, giving you an idea of the data's dispersion.

This type of plot is useful for comparing the central tendency (mean) and variability (standard deviation) of 'Sales' across different 'Market Size' categories.
"""

#BARPLOT

sns.barplot(data=df, x='Market Size', y='Sales', estimator=np.mean, errorbar='sd');

sns.barplot(data=df, x='Market Size', y='Sales', estimator=np.mean, errorbar='sd', hue='Market');

