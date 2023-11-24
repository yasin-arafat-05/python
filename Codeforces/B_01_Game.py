t = int(input())
for _ in range(t):
    s = str(input())
    one = 0
    zeros = 0
    for i in range(len(s)):
        if s[i]=='0':
            zeros +=1
        else:
            one +=1
    if(min(zeros,one)%2==0):
        print('NET')
    else:
        print('DA')