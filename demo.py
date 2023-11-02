 
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


#------------------------------------PATTERN PROBLEM 
# Pattern 1: Right Triangle
for i in range(1, 6):
    print("*" * i)

# Pattern 2: Upside-Down Right Triangle
for i in range(5, 0, -1):
    print("*" * i)

# Pattern 3: Hollow Rectangle
width = 5
height = 4
for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")

# Pattern 4: Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Pattern 5: Diamond
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Pattern 6: Inverted Pyramid
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Pattern 7: Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 8: Pascal's Triangle
def generate_pascals_triangle(n):
    def generate_next_row(prev_row):
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        return new_row

    triangle = []
    row = [1]
    triangle.append(row)
    for _ in range(n - 1):
        row = generate_next_row(row)
        triangle.append(row)

    return triangle

n = 5
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(" ".join(map(str, row)).center(n * 3))

# Pattern 9: 180-Degree Rotated Right Triangle
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

# Pattern 10: Number Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(map(str, range(i, 0, -1))) + " ".join(map(str, range(2, i + 1)))


#__________________________________________________matrix____________________
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix dimensions must match for addition.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix dimensions must match for subtraction.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0]):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    
    return result

# Define two example matrices
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Print the matrices
print("Matrix A:")
print_matrix(matrix_A)

print("\nMatrix B:")
print_matrix(matrix_B)

# Perform matrix operations
matrix_sum = add_matrices(matrix_A, matrix_B)
matrix_diff = subtract_matrices(matrix_A, matrix_B)
matrix_product = multiply_matrices(matrix_A, matrix_B)

# Print the results
print("\nMatrix Sum (A + B):")
print_matrix(matrix_sum)

print("\nMatrix Difference (A - B):")
print_matrix(matrix_diff)

print("\nMatrix Product (A * B):")
print_matrix(matrix_product)
