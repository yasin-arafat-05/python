####################QUESTION PART##################
'''
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
'''
####################SOLUTION PART##################
n = int(input("enter a number: "))
list = []
for i in range(n+1):
    if(i%2!=0):
        list.append(i)

print(f"ODD NUMBER LIST: {list}")
