#Here we have to print on the gap of number and in a triangular pattern here we have to take an spaces in this function by tsking s is spaces 
n = int(input())
for i in range(1, n + 1, 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(i, 2 * i, 1):
        print(j, end="")
    for j in range(2*i - 2, i - 1, -1):
        print(j, end="")
    print()

