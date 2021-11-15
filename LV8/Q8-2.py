N = int(input())
if N == 1:
    print(N)
else:
    cnt = 2
    num = 2
    while N not in range(num, num + 6 * (cnt - 1)):
        num = num + 6 * (cnt - 1)
        cnt += 1
    print(cnt)


# Q8-3처럼 while 안돌리고 할수 있을듯.