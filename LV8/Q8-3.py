X = int(input())
if X == 1:
    print("1/1")
else:
# 1 + 2 + ... + n = n(n + 1) / 2
# n(n + 1) / 2 >= X인 최소 n
    cnt = 2
    while cnt * (cnt + 1) < 2 * X:
        cnt += 1
    x = cnt * (cnt + 1) // 2 - X + 1
    if cnt % 2:
        print("{}/{}".format(x, cnt - (x - 1)))
    else:
        print("{}/{}".format(cnt - (x - 1), x))