def prost(a,m = []):
    if a == 1:
        return True
    for i in m:
        if a % i == 0:
            return False
    m.append(a)
    return True
i = 1
a = 0
while a < 10002:
    if prost(i):
        a += 1
    i += 1
print(i-1)