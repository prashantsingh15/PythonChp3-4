n =int(input())
flag = False 
for d  in range(2,n,1):
    if n%d==0:
        flag =True
        break

if flag:
    print("Not Prime")

else:
    print("Prime")