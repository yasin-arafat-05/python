#download a csv (comma seperated values)

import urllib.request
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

#(url,file name <download> )
urllib.request.urlretrieve(italy_covid_url,'covid_italy.csv')

import pandas as pd 

covid_df = pd.read_csv('./covid_italy.csv')
print(f"-----------Type of covid_df.csv file: --------- \n {type(covid_df)}")
print()

print("-----------Information (.info()) covid_df.csv file: --------- \n }")
#information about of covid_df file 
print(covid_df.info())


#descrive the  numerical data only
print("------------------describe the numerical data---------------")
print(covid_df.describe())


#find the colunm property or metadata
print()
print("------------------Descrive the column data---------------")
print(covid_df.columns)

#find the shape of the dataFrame
print()
print("------------------Shape Of the dataFrame---------------")
print(covid_df.shape)

'''
Here's a summary of the functions & methods we've looked at so far:

pd.read_csv - Read data from a CSV file into a Pandas DataFrame object.
.info() - View basic infomation about rows, columns & data types.
.describe() - View statistical information about numeric columns.
.columns - Get the list of column names.
.shape - Get the number of rows & columns as a tuple.
'''
