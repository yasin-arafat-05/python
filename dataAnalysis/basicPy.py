#problem: 01
'''
#A grocery store sells a bag of ice for $1.25 and makes a 20% profit.
#If it sells 500 bags of ice, how much total profit does it make?
'''
print("--------------------------Problem: 01-------------------------------")
profit = 500*(1.25)*(20/100)
print("Total profit: ",profit)

#problem: 02
'''
A travel company wants to fly a plane to the Bahamas.
Flying the plane costs 5000 dollars. So far, 29 people have signed up for the trip.
If the company charges 200 dollars per ticket, what is the profit made by the company? 
Create variables for each numeric quantity and use appropriate arithmetic operations.
'''
print("--------------------------Problem: 02-------------------------------")
plane_cost = 5000
total_earn = (200*29)
print("Profit: ",(total_earn-plane_cost))


#problem: 03
'''
multiline_string = """a
b"""
find the length of the multiline string
'''
print("--------------------------Problem: 03-------------------------------")
multiline_string = """a
b"""
print(len(multiline_string))
multiline_string_list = list(multiline_string)
print(multiline_string_list) # that's why we get the length 3.


#problem: 04
'''
check int the string today = "Saturday"
we have if you have 'Sa', 'day', 'Tu'.
'''
print("--------------------------Problem: 04-------------------------------")
today = "Saturday"
print(f"{'Sa' in today} <----------> {'day' in today} <--------> {'Tu' in today}")

name = "Yasin Arafat"
age = 25
string_value = '''this is {} and age {}'''
print(string_value.format(name,age))
print("this is "+str(name)+" and age is: "+str(age))

#Iteration with for loops
'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

'''
print("--------------------------Problem: 05-------------------------------")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for k in days:
    print(k,end=" ")
print()
person = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}
for key in person.keys():
    print(key,end=" ")
print()
for value in person.values():
    print(value,end=" ")
print()

for keys,values in person.items():
    print(f"key: {keys} and values: {values}")
print()
a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for i, val in enumerate(a_list):
    print('The value at position {} is {}.'.format(i, val))

#problem: 6 
#solve with functoin.
'''
Try-except:
divison by 0
'''
print("--------------------------Problem: 06-------------------------------")

def devision(x:int):
    try:
        ans = 5/x
        print(f"ans: {ans}")
    except:
        print("divisible by 0")
devision(0)

#problem:07
#Documenting functions using Docstrings
'''
write a program. substraction of two number and Use DocString.
'''
print("--------------------------Problem: 07-------------------------------")

def subtracation(x:int,y:int):
    """
    x -> first number.
    y -> second number.
    here, x>y
    """
    help(subtracation)
    diff = x -y 
    print("subtraction: {}".format(diff))
subtracation(45,5)