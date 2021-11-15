T = int(input())

def hotel_num(H, W, N):
    f = N % H
    d = N // H + 1
    if not f:
        f = H
        d -= 1
    return "{}".format(f) + "{:0=2d}".format(d)

for i in range(T):
    print(hotel_num(*map(int, input().split())))