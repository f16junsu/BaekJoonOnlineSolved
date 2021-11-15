from math import sqrt
N = int(input())
i = 2
if N == 1:
    pass
else:
    while i <= int(sqrt(N)):
        if N % i == 0:
            print(i)
            N = N // i
        else:
            i += 1
    print(N)