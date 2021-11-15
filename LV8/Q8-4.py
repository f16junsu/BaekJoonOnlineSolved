from math import ceil
A, B, V = map(int, input().split())
day = 1
if V <= A:
    print(1)
else:
    print(day + ceil((V - A) / (A - B)))
    