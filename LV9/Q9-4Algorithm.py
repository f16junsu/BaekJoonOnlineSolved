M, N = map(int, input().split())
ls = [False, False] + [True] * (N - 1)
for i in range(2, int(N**.5) + 1):
    if ls[i]:
        for j in range(2 * i, N, i):
            ls[j] = False
for i in range(N + 1):
    if ls[i] and i >= M:
        print(i)