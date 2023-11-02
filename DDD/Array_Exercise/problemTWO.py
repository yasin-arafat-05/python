####################QUESTION PART##################
'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

Using this find out,
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
####################SOLUTION PART##################

heros=['spider man','thor','hulk','iron man','captain america']

print(f"length of the array is : {len(heros)}")

heros.append("black panther")

print(f"After appending \"black panther\" : {heros}")

heros.remove("black panther")
heros.insert(3,"black panther")


print(f"After appending \"black panther\"  after hulk : {heros}")
heros.remove("black panther")

#or instead of below two lines we can use
#heros[1:3]=['doctor strange']

heros[1] = "doctor strange"
heros[2] = "doctor strange"

print(f"Removing \"thor and hulk\": {heros}")

#soring  in alphabetically order
heros.sort()
print(f"After sorting: {heros}")