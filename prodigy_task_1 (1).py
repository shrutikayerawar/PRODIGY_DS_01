# -*- coding: utf-8 -*-
"""PRODIGY TASK 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gDR__dz5iNqPS69Los88SaCY1jlnelbA
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import pandas as pd
df=pd.read_csv("/content/Population.zip")

df

import seaborn as sns

df1=df.groupby("Continent")[["2022 Population"]].sum()
df1
df1["2022 Population"]
sns.barplot(x=df1.index,y=df1["2022 Population"],order=["Asia","Africa","Europe","North America","South America",
                                                      "Oceania" ],alpha=0.8,)

df2=df[df["Continent"]=="Asia"]
df3=df2[df2["2022 Population"]>100000000]
df4=df3[df3["Density (per km²)"]>100]
sns.barplot(x="Country/Territory",y="2022 Population",data=df4).set(title="Asian overpopulated Country")

df2=df[df["Continent"]=="Africa"]
df3=df2[df2["2022 Population"]>50000000]
df4=df3[df3["Density (per km²)"]>100]
sns.barplot(x="Country/Territory",y="2022 Population",data=df4).set(title="African overpopulated Country")

df2=df[df["Continent"]=="Europe"]
df3=df2[df2["2022 Population"]>50000000]
df4=df3[df3["Density (per km²)"]>100]
sns.barplot(x="Country/Territory",y="2022 Population",data=df4).set(title="Europian overpopulated Country")

import matplotlib.pyplot as plt

x=df["Continent"]=="Asia"
d1=df[x]
d2=d1[d1["2022 Population"]>100000000]
d3=d2[d2["Density (per km²)"]>100]
plt.pie(d3["2022 Population"],labels=d3["Country/Territory"],autopct="%0.1f%%")
plt.show()

import numpy as np
l=[]
df1=df[df["Country/Territory"]=="China"]
x=df1.filter(items=["2022 Population","2020 Population","2015 Population","2010 Population","2000 Population",
                   "1990 Population","1980 Population","1970 Population"])
for i in x.values:
    l.append(i)
print(l[0])
x.columns
plt.bar(x.columns,l[0])
plt.xticks(rotation=90)
plt.yticks(l[0])
plt.grid()
plt.show()

x=df["Rank"]<10
df1=df[x]
sns.barplot(y=df1["World Population Percentage"],x=df1["Country/Territory"])
plt.title("top 10 world populated country")
plt.xticks(rotation=90)
plt.show()

x=df["Area (km²)"]>3000000
df1=df[x]
df1
sns.barplot(x=df1["Country/Territory"],y=df1["Density (per km²)"])
plt.show()
sns.barplot(x=df1["Country/Territory"],y=df1["Area (km²)"])

df["popoulation_diff"]=df["2022 Population"]-df["1970 Population"]
x=df["popoulation_diff"]>100000000
df1=df[x]
plt.figure(figsize=(9,5))
sns.barplot(y=df1["popoulation_diff"],x=df1["Country/Territory"])
plt.title("population difference greater than 10Cr")

