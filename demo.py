 
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
