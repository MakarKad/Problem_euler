def podil(a):
    for i in range(1,20):
        if a % i != 0:
            return False
    return True

i = 20
while 1:
    if podil(i):
        print(i)
        break
    i += 20