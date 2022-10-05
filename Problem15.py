N = int(input()) + 1
a = [[1,*['p'] * (N-1)] if i != 0 else [1] * (N) for i in range(N)]
for i in range(1,N):
    for j in range(1,N):
        a[i][j] = a[i-1][j] + a[i][j-1]
print(a[-1][-1])