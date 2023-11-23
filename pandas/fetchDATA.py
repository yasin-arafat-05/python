#<-----------------------------------How pandas store data---------------------------------------->

# Pandas format is simliar to this
#This is take less memory then the given below using list.
covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}


# Pandas format is not similar to this
#this take more memory because in the list we have a bunch of dictionary.
#and in this diction everytime we give the 'data' as key. As it takes more memory 
#then the performance will decrease than the first_ONE.

covid_data_list = [
    {'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
    {'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
    {'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
    {'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
    {'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
]




#<--------------------------------------------------------------------------------------->
from  introduction import covid_df

print('<----------------new cases---------------->')
print(covid_df['new_cases'])
print()
print(f"simillarly: \n {covid_df.new_cases}")
print()
print("<------------Type of new_cases data--------------->")
print(type(covid_df['new_cases']))

print()
print("<--------fetch single data from new_cases----------->")
print(covid_df['new_cases'][55])

print()
print("<----------------We can do the same with .at[] list------------------->")
print(covid_df.at[55,'new_cases'])


print()
print("<----------------------------------Access Multiple Column---------------------------->")
print(covid_df[['new_cases','new_tests']])
print(covid_df.at[243,'new_tests'])
print(f"<--------------------fetch a single column:---------------------> \n {covid_df.loc[243]}")


print()
print("<----------------fetch first five values from the covid_df---------------------->")
print(covid_df.head(5))


print()
print("<----------------fetch last five values from the covid_df---------------------->")
print(covid_df.tail(5))


print()
print("<--------------------type of NaN ---------------------------->")
print(covid_df.loc[1,"new_tests"])
print(type(covid_df.loc[1,"new_tests"]))


print()
print("<----------- first index that doesn't contain-------------->")
print(f"{covid_df.new_tests.first_valid_index()}")
print()
print(f"{covid_df.loc[109:113]}")

print()
print("<-------------Randomly fetch data-------------->")
print(f"{covid_df.sample(10)}")

'''
Here's a summary of the functions & methods we looked at in this section:
covid_df['new_cases'] - Retrieving columns as a Series using the column name
new_cases[243] - Retrieving values from a Series using an index
covid_df.at[243, 'new_cases'] - Retrieving a single value from a data frame
covid_df.copy() - Creating a deep copy of a data frame
covid_df.loc[243] - Retrieving a row or range of rows of data from the data frame
head, tail, and sample - Retrieving multiple rows of data from the data frame
covid_df.new_tests.first_valid_index - Finding the first non-empty index in a series
'''