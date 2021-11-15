T = int(input())
def issosu(i):
    if i == 1:
        return False
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            return False
    return True

ls = list(map(int, input().split()))
cnt = 0
for n in ls:
    if issosu(n):
        cnt += 1
print(cnt)