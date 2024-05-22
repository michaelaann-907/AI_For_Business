# -*- coding: utf-8 -*-
"""CodeAlong4Pandas.ipynb

Automatically generated by Colab.


# Pandas

Created September 11, 2023

https://pandas.pydata.org/

Pandas is a Python library for data manipulation and analysis, particularly well-suited for working with structured data like tables and spreadsheets.
"""

import numpy as np
import pandas as pd

my_idx = ["NY", "CA", "NC"]  # creating an index

my_data = [15, 25, 10]  # population

type(my_data)

"""
A Pandas Series is a one-dimensional labeled array-like data structure provided by the Pandas library in Python. 
It is similar to a column in a spreadsheet or a single column in a SQL table. 
Each element in a Series can hold data of any data type, including numbers, strings, and even more complex objects.
"""

my_series = pd.Series(data=my_data)  # convert list to pandas series
my_series

type(my_series)

my_series = pd.Series(data=my_data, index=my_idx)
my_series

my_series["NC"]

my_series[2]  # can access NC with the index number as well // index is 2

"""
0 NY 15

1 CA 25

2 NC 10
"""

# Dictionary of 3 Stocks
stocks = {"AAPL": 178.25, "NVDA": 455.20, "CSO": 56.17}

type(stocks)

stock_series = pd.Series(stocks)
stock_series

type(stock_series)

stock_series['AAPL']

stock_series[0]

# Quarterly Sales $Million // Use curly brackets
q1 = {'AAPL': 200, 'NVDA': 80, 'CSC': 150}
q2 = {'AMZN': 270, 'NVDA': 70, 'CSCO': 175}

type(q1)

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print('Type for q1 :', type(q1))
print('Type for q2:', type(q2))

sales_q1[0]

sales_q1

sales_q2

sales_q1.keys()

# BROADCASTING
sales_q1 * 2

sales_q2 / 100

sales_q1 + sales_q2

sales_q1.add(sales_q2, fill_value=0)