a = open('names.txt', 'r', encoding='utf-8')
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
a = sorted(a.readline().replace('"', "").split(','))
c = 0
for i, value in enumerate(a):
    c += sum([b.index(j) + 1 for j in value]) * (i + 1)
print(c)
