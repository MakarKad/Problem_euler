import math
N=1000000
prime=[True] * 1000000
prime[0], prime[1] = False, False
for i in range(2,int(math.ceil(math.sqrt(N)))):
    if prime[i]:
        j= i * i
        while j < N:
            prime[j] = False
            j += i
a = 0
for i,value in enumerate(prime):
    if value and 600851475143 % i == 0 and a < i:
        a = i
print(a)







