from math import sqrt

M, N = map(int, input().split())
Ls = [2] + [n for n in range(2, N + 1) if n % 2 != 0]
ls = []
while Ls:
    num = Ls.pop(0)
    if (num >= sqrt(N)):
        ls = ls + Ls
        break
    ls.append(num)
    Ls = list(filter(lambda x : x % num != 0, Ls))
for i in list(filter(lambda x : x >= M, ls)):
    print(i)