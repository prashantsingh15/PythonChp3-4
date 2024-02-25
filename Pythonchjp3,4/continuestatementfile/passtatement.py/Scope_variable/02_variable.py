a2 = 10   # Global variable 
def f2():
    b2 = 12   # Local Variable 
    print(b2)
    print(a2)   # <--- Here we can print the value of a2 again 

print(a2)

f2()