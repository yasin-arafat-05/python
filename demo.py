 
k = 34
l = 45.5
m = "yasin Arafat"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHAPTER_TWO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("_________DATA TYPE________")
print(type(k))
print(type(l))
print(type(m))

print("_________TYPE CASTING_______")
k = str(k)
print(type(k))
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHAPTER_THREE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("_________STRING______________")
n = "Yasin Arafat"
n = n.capitalize()  #capitalize only first character
print(n)
print(n[:])
print(n[0:])
print(n[:])
print(n[3:])
print(n[0:6:3])
print(f"number of count of a: {n.count('a')}")
print(n.endswith("arafat"))
print(f"return the index of ar {n.find('ar')}")
print(f"len of the string : {len(n)}")
print(f"type of n : {type(n)}")
print(n.replace('ar','Ar'))
n = n + " khan"
print(n)
#----------------------------------------------------
# Hello World
print("Hello, World!")

# Variables and Data Types
age = 30
name = "John"
is_student = True
height = 5.9
favorite_colors = ["blue", "green", "red"]

# Conditional Statements
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Loops
for color in favorite_colors:
    print(f"My favorite color is {color}.")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet(name))

# Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])

# Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())

# Input and Output
user_input = input("Enter a number: ")
user_number = int(user_input)
print(f"You entered: {user_number}")

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Division by zero"
print(result)

# File I/O
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")

with open("sample.txt", "r") as file:
    contents = file.read()
print(contents)

#-------------------------------------------------

# String Manipulation
string_variable = "Python is fun!"
uppercase_string = string_variable.upper()
substring = string_variable[7:10]
print(uppercase_string)
print(substring)

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# Tuples
coordinates = (3, 4)
x, y = coordinates
print(f"X: {x}, Y: {y}")

# Sets
fruits = {"apple", "banana", "orange"}
fruits.add("grape")
print(fruits)

# Importing Modules
import math
print(math.sqrt(25))

# Conditional Expressions (Ternary Operator)
a = 5
b = 10
max_value = a if a > b else b
print(max_value)

# Lambda Functions
multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)

# File Handling (Appending to a File)
with open("sample.txt", "a") as file:
    file.write("\nThis is an appended line.")

with open("sample.txt", "r") as file:
    updated_contents = file.read()
print(updated_contents)
