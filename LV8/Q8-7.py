N = int(input())
f = N // 5
t = 0
while True:
    if f == 0:
        if N % 3 != 0:
            print(-1)
            break
        else:
            print(N // 3)
            break
    else:
        left = N - (f * 5)
        if left % 3 == 0:
            print(f + left // 3)
            break
        else:
            f -= 1