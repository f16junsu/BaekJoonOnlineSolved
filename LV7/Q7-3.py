S = input()
l = "abcdefghijklmnopqrstuvwxyz"
result = []
for c in l:
    S = list(S)
    ind = -1
    try:
        ind = S.index(c)
    except ValueError:
        pass
    result.append(ind)
for i in result:
    print(i, end=' ')