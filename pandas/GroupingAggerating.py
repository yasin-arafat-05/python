import urllib.request
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urllib.request.urlretrieve(italy_covid_url,"italy_covid.csv")

import pandas as pd
italy_covid = pd.read_csv("./italy_covid.csv")


italy_covid["date"] = pd.to_datetime(italy_covid.date)
italy_covid["month"] = pd.DatetimeIndex(italy_covid.date).month


'''
Without .sum() method it return an object 
'''
print("__________________________________ Month Sum__________________________________")
group_by_month = italy_covid.groupby('month')[["new_cases","new_deaths","new_tests"]].sum()
print(group_by_month)

print()
print()
print("__________________________________ Weakday Mean__________________________________")
italy_covid["weekday"] = pd.DatetimeIndex(italy_covid.date).weekday
group_by_mean = italy_covid.groupby('weekday')[["new_cases","new_deaths","new_tests"]].mean()
print(f"    {group_by_mean}  ")


italy_covid["total_cases"] = italy_covid.new_cases.cumsum()
italy_covid["total_deaths"] = italy_covid.new_deaths.cumsum()
italy_covid['total_tests'] = italy_covid.new_tests.cumsum()

print()
print()
print(f" __________________________________ cumsum()  method: __________________________________ \n {italy_covid}") 


print()
print()
print()
print()

print(f" __________________________________  Adding data from another source  __________________________________ ") 

urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')
location = pd.read_csv("./locations.csv")

print("------the locaiton of Itally---------")
location_itally = location[location.location == "Italy"]
print(location_itally)
print(f" __________________________________  Adding Location in italy_covid file  __________________________________ ") 

italy_covid["location"] = "Italy"

print()
print()

print(f" __________________________________  Merge the  location of italy information in  italy_covid file  __________________________________ ") 

'''
To merge up: we should have a common column: That's why we create the location
column in the italy_covid file.
And now we merge the information of the location file
'''
merge_df = italy_covid.merge(location, on="location")
print(merge_df)

print()
print()
merge_df["cases_per_million"] = (merge_df.total_cases*1e6) / (merge_df.population)
merge_df["deaths_per_million"] = (merge_df.total_deaths*1e6) / (merge_df.population)
merge_df["tests_per_million"] = (merge_df.total_tests*1e6)/(merge_df.population)
print(merge_df)

print()
print()
print("-------------now we save the file and the column that really need for me collect this column only-------------")

result_df = merge_df[[
    'date',
    'new_cases',
    'total_cases',
    'new_deaths',
    'total_deaths',
    'new_tests',
    'total_tests',
    'cases_per_million',
    'deaths_per_million',
    'tests_per_million'
]]

print()
print()
print()
print(result_df)

result_df.to_csv('result.csv', index=False)


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
####################################################################################################
##########################Pandas give a .plot() mehtod to draw a line graph#########################
####################################################################################################
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


result_df.new_cases.plot()
