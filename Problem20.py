a = 1
for i in range(1,101):
    a *= i
b = 0
for i in str(a):
    b += int(i)
print(b)