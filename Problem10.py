import math
N=2000000
prime=[True] * N
prime[0], prime[1] = False, False
for i in range(2,int(math.ceil(math.sqrt(N)))):
    if prime[i]:
        j= i * i
        while j < N:
            prime[j] = False
            j += i
b = 0
for i,value in enumerate(prime):
    if value:
        b += i
print(b)