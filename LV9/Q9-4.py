M, N = map(int, input().split())
Ls = [n for n in range(2, N + 1) if n % 2 != 0]
ls = []
while Ls:
    ls.append(Ls.pop(0))
    Ls = list(filter(lambda x : x % ls[-1] != 0, Ls))
    if ls[-1] >= M:
        print(ls[-1])