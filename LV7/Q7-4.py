def f(n, st):
    news = ''
    for c in st:
        for i in range(n):
            news = news + c
    return news


T =  int(input())
for i in range(T):
    r, s = input().split()
    r = int(r)
    print(f(r, s))
