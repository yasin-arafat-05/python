import os

#get the current working directory

print(os.getcwd())

#What files are present in current directory
print(os.listdir('.'))


#what files are present in /usr directory
print(os.listdir('/usr'))
#print(os.listdir('/usr/bin'))

#make a new dirctory in current directory 
os.makedirs('./data',exist_ok=True)

#check the data directory is empty or not 

os.listdir('./data')