M, N = map(int, input().split())
Ls = [2, 3, 5, 7, 11] + [n for n in range(4, N + 1) if not 
               (n % 2 == 0 or 
                n % 3 == 0 or
                n % 5 == 0 or
                n % 7 == 0 or
                n % 11 == 0)]
while Ls:
    if Ls[0] == 0:
        Ls.pop(0)
        continue
    else: 
        num = Ls.pop(0)
        if num >= M:
            print(num)
        Ls = list(map(lambda x: 0 if x % num == 0 else x, Ls))
