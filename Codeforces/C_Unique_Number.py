t = int(input())
for _ in range(t):
    x = int(input())
    ans = ''
    if(x>45):
        print(-1)
    elif x<=9:
        print(x)
    else:
        for i in range(9,0,-1):
            if(x<9 and x<=i):
                ans +=str(x)
                rans = ans[::-1]
                print(rans)
                break
            else:  
                ans +=str(i)
                x -=i
                