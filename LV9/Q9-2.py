def issosu(i):
    if i == 1:
        return False
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            return False
    return True

M = int(input())
N = int(input())

ls = []
for i in range(M, N + 1):
    if issosu(i):
        ls.append(i)

if ls:
    print(sum(ls))
    print(ls[0])
else:
    print(-1)