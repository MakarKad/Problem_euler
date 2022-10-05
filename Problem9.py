a = 0
b = 0
c = 0
for i in range(1,1000):
    for j in range(1,1000):
        c = (i ** 2 + j ** 2) ** 0.5
        if i + j + c == 1000:
            a = i
            b = j
            break
    if a + b + c == 1000:
        break
print(int(a * b * c))