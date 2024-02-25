a4 = 13

def f4():
    
    global a4

    a4 = 12

    print(a4)

    print(id(a4))

print(a4)

f4()

print(a4)

print(id(a4))