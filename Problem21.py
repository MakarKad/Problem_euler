a = 0
b = []
for i in range(1, 10000):
    dil1 = sum([j for j in range(1, i) if i % j == 0])
    dil2 = sum([j for j in range(1, dil1) if dil1 % j == 0])
    if i == dil2 and dil2 not in b and i != dil1:
        b.append(dil1)
        a += (dil1 + i if dil1 < 10000 else i)
print(a)
