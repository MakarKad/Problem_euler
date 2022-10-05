m1 = 0
m2 = 1
for i in range(100):
    m1 += i**2
    m2 += i
print(m2 ** 2 - m1)