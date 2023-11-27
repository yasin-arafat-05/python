import urllib.request

italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urllib.request.urlretrieve(italy_covid_url,"covidItaly.csv")
import pandas as pd
covid_report = pd.read_csv("covidItaly.csv")
print(covid_report)

print("____________________See the cases which have ")