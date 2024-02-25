# <-------Cant print a local variable outside the function print (b1) ------->

a1 = 10       # Global  variable 

def f1():
    b1=12      #Local variable 
    print(b1)

print(a1)
f1()
