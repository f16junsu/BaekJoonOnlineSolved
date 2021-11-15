M, N = map(int, input().split())
ls = []
Ls = [n for n in range(2, N + 1)]
while Ls:
    if Ls[0] == 0:
        Ls.pop(0)
        continue
    else: 
        num = Ls.pop(0)
        ls.append(num)
        for ind in range(len(Ls)):
            if Ls[ind] % num == 0:
                Ls[ind] = 0
ind = 0
for i in range(len(ls)):
    if ls[i] >= M:
        ind = i
        break
ls = ls[ind:]
for i in ls:
    print(i)