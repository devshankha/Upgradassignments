#univariate analysis, mean after removing outliers upto 95th percentile
import numpy as np
import pandas as pd
import os
print(os.getcwd())
inp = pd.read_csv("popularity.csv")

#this is very important, sometimes while reading a csv file, the columns might have some spaces
#this command is very useful to remove spaces in between the column names

inp.rename(columns=str.strip, inplace=True)
#inp.info()
#extracting a particular column from a database
k = inp[['shares']]
print(k.describe())
print("--------")
#keeping values upto 95th percentile
k = k[k.shares <= k.shares.quantile(.95)]
print(k.describe())

ss = k['shares']
print(np.std(ss))
