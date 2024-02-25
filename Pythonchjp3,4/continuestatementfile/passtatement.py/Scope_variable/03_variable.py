# <----- You can access any global Variable defined  before tyhe function call ------->

def f3():

    b3 = 12    # Global Variable 

    print(b3)

    print(a3)

    # print(c3)

a3 = 10     # Local Variable 

print(a3)

f3()

# c3 = 20
