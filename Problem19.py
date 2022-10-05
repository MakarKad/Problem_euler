a = 0
b = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if j == 2:
            b += 29 if i % 4 == 0 else 28
        elif j % 2 == 0:
            b += 30
        else:
            b += 31
        a += 1 if b % 7 == 0 else 0
print(a)
