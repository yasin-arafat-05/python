import urllib.request
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urllib.request.urlretrieve(italy_covid_url,"covid_in_italy.csv")

#read csv file
import pandas as np 
covid_Itely = np.read_csv('./covid_in_italy.csv')
print(covid_Itely)

print("___________________Sum-of-a-column_________________")
print(f"sum of total deaths \n {covid_Itely.new_deaths.sum()}") 

#NaN values get ignored.
print(f"sum of total new_cases \n {covid_Itely.new_cases.sum()}")
date_rate = (covid_Itely.new_deaths.sum()/covid_Itely.new_cases.sum() )*100
print("date rate: \n {:.2f}%".format(date_rate))

