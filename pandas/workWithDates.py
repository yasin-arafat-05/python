import urllib.request

italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urllib.request.urlretrieve(italy_covid_url,"covid_italy.csv")

import pandas as pd
covid_db = pd.read_csv("./covid_italy.csv")

print(covid_db.date)

print("--------here pandas identify date as date it show the dtype as object----------")
print("-----------------------we need to convert this into date time---------------------------")
covid_db["date"] = pd.to_datetime(covid_db.date)

print(f"see the type of date now : \n {covid_db.date}")

covid_db['Year'] = pd.DatetimeIndex(covid_db.date).year
covid_db['Month'] = pd.DatetimeIndex(covid_db.date).month
covid_db["Day"] = pd.DatetimeIndex(covid_db.date).day
covid_db["Weekday"] = pd.DatetimeIndex(covid_db.date).weekday

print(covid_db)


print()
print()
print()

print("------------Query the value of any month-------------")
covid_db_month = covid_db[covid_db.Month == 5]
print(f"In the month of may :\n {covid_db_month}")

#now find the total new_cases, new_deaths,new_tests in the month of may 
print()
print()
print()

covid_db_month_may = covid_db_month[['new_cases','new_deaths','new_tests']]
print(covid_db_month_may)

covid_db_month_may = covid_db_month_may.sum()
print(covid_db_month_may)

'''
we can also done this by one statement: 
covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
'''

# Average for Sundays
sunday = covid_db[covid_db.Weekday == 6].new_cases.mean()
print(f"sunday new_cases average -> {sunday}")

