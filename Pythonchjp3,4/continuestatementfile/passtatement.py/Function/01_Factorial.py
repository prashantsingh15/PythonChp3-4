# This code is so complicated soo dont use this code because its for only example so the another codew is for that so use it....
n = int(input())
r = int(input())

n_fact = 1
for i in range(1, n + 1):
    n_fact = n_fact * i
    
r_fact = 1
for i in range(1, r + 1):
    r_fact = r_fact * i

n_r_fact = 1
for i in range(1, n - r + 1):
    n_r_fact = n_r_fact * i

ans = n_fact//(r_fact * n_r_fact)
print(ans)



