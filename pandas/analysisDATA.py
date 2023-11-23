import urllib.request
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urllib.request.urlretrieve(italy_covid_url,"covid_in_italy.csv")

#read csv file
import pandas as np 
covid_Itely = np.read_csv('./covid_in_italy.csv')
print(covid_Itely)
