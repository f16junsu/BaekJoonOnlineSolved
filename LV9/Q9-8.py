p1x, p1y = map(int, input().split())
p2x, p2y = map(int, input().split())
p3x, p3y = map(int, input().split())

def single(a, b, c):
    if a == b:
        return c
    elif b == c:
        return a
    else:
        return b

print(single(p1x, p2x, p3x), single(p1y, p2y, p3y))