def stars(N):
    if N == 1:
        return ["*"]
    else:
        n = N // 3
        ls = stars(n)
        L = [s * 3 for s in ls] + \
            [s + " " * n + s for s in ls] + \
            [s * 3 for s in ls]
        return L

N = int(input())
for s in stars(N):
    print(s)