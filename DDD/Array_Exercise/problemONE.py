
####################QUESTION PART##################
'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
####################CODING PART##################
expense = [2200,2350,2600,2130,2190]

print(f"Extra spent compare to January = {expense[1]-expense[0]}")

print(f"Expense in first three months: {expense[0]+expense[1]+expense[2]}")

k = -1
for i in range(len(expense)):
    if(expense[i]==2000):
        if(i==0):
            print("January")
        elif(i==1):
            print("February")
        elif(i==2):
            print("March")
        elif(i==3):
            print("April")
        elif(i==4):
            print("May")
    else:
        k = 1
if(k==1):
    print("Not any month found expenses 2000")

#append -> সংযোজন

expense.append(1980)
print(f"new list: {expense}")

expense[3] = expense[3] - 200
print(f"refunding 200 dolar : {expense}")


