a = 0
for i in  range(100,1000):
    for j in range(100,1000):
        if i * j == int(str(i * j)[::-1]):
            a = i * j if  a < i * j else a
print(a)
