# -*- coding: utf-8 -*-

import pandas as pd

url="https://raw.githubusercontent.com/yamini542/Data-Analysis-Practice_Day1/refs/heads/main/sales_data.csv"

data = pd.read_csv(url)

data.head()

data.shape

print(data)

data.info() #calling the info method

print(data.info()) #we are referring to the info method

#Step4:
#Analyze data
sales_by_region = data.groupby('Region')['Sales'].sum()

"""The difference between ('Region') and ["Sales"]  the first set tell the pandas to groupby region with same values and another one is used to select the sales column from each group.

"""

sales_by_region

top_products=data.groupby("Sales")['Product'].sum()

top_products=

top_products=top_products.sort_values(ascending=False).head(5)

top_products

import matplotlib.pyplot as plt

sales_by_region.plot(kind='bar',color='skyblue')
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.show()

