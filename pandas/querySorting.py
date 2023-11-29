import urllib.request

italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urllib.request.urlretrieve(italy_covid_url,"covidItaly.csv")
import pandas as pd
covid_report = pd.read_csv("covidItaly.csv")
print(covid_report)

print("____________________See the cases which have greater than 1000 new_cases identified____________________")

new_case_grater_thousand = covid_report.new_cases > 1000
print(f" -------grater than 1000 (true\false) ------- \n {new_case_grater_thousand}")
print(f"now print the value where only satisfied the condition: \n{covid_report[new_case_grater_thousand]}")
'''
----- we can do the same with: -----
high_cases_df = covid_df[covid_df.new_cases > 1000]
'''
print()
print()
print("____________________See All the data____________________")

from IPython.display import display
with pd.option_context('display.max_row',72):
    display(covid_report[covid_report.new_cases > 1000])

'''
Question: 
What is the overall number of tests conducted?
 A total of 935310 tests were conducted before daily test numbers were reported.
'''
initial_tests = 935310
total_tests = initial_tests + covid_report.new_tests.sum()
print(f"-----Overall test conducted----- \n {total_tests}")

'''
What fraction of tests returned a positive result?
'''
print()
positive_rate = covid_report.new_cases.sum() / total_tests
print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate*100))

print()
print("%------Where the dected number of person is greater than the average ------%")
high_ratio_df = covid_report[covid_report.new_cases / covid_report.new_tests > positive_rate]
print(high_ratio_df)

print("-----------------Add the positive rate in covid_report-----------------")
covid_report["positive_rate"] = covid_report.new_cases/covid_report.new_tests
print(covid_report)


print("---delete the positive_rate column ----")
covid_report.drop(columns="positive_rate",inplace=True)
print(covid_report)


print()
print()
print()

print("-----------------Soting Values-----------------")
k = covid_report.sort_values("new_cases",ascending=True).head(10)
print(f" {k} ")

print(f"{covid_report.loc[170:174]}")


'''
This is data entry error: We can't get the number negative.
To sort out this problem we can replace the value with an average number.
here we will do: (index: 171 + index: 172)/2 
'''
covid_report.at[172,"new_cases"] = (covid_report.at[171,"new_cases"] + covid_report.at[173,"new_cases"])/2

print(f"Modifing the value : \n {covid_report.loc[170:174]}")


#################################################################################################
# Summary of the session: 
''''
Here's a summary of the functions & methods we looked at in this section:

covid_df.new_cases.sum() - Computing the sum of values in a column or series
covid_df[covid_df.new_cases > 1000] - Querying a subset of rows satisfying the chosen criteria using boolean expressions
df['pos_rate'] = df.new_cases/df.new_tests - Adding new columns by combining data from existing columns
covid_df.drop('positive_rate') - Removing one or more columns from the data frame
sort_values - Sorting the rows of a data frame using column values
covid_df.at[172, 'new_cases'] = ... - Replacing a value within the data frame
'''
##################################################################################################