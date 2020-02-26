'''
Date: 2020-02-24
Author: SC

Below code can be used for analysis of FIFA 2019 datset.
'''

import numpy as np 
import pandas as pd 

#to view all columns while 
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', None)

import scipy
#to re-scale the data
from sklearn.preprocessing import MinMaxScaler

#FIFA 2019 csv file path and name
file_name = 'data.csv'
file_path = r'C:\Users\schettri\Documents\Python Scripts\FIFA 2019'

#read csv file and store it in a dataframe
dataframe = pd.read_csv(file_path + '\\' + file_name)

#read first 5 lines of the datafrane
dataframe.head()

#column infos
dataframe.info()

#presents basic stats on the columns
dataframe.describe()

#Re-scaling the data
#https://medium.com/greyatom/why-how-and-when-to-scale-your-features-4b30ab09db5e


