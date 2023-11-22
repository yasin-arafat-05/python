r,c = map(int,input().split())
b = 0
w = 0
g = 0
oc = 0
for i in range(r):
    k = list(input().split())
    for c in k:
        if(c=="B"):
            b +=1
        elif(c=="W"):
            w +=1
        elif(c=="G"):
            g +=1
        else:
            oc +=1
if(oc!=0):
    print("#Color")
else:
    print("#Black&White")