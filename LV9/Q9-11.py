from math import dist
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = dist((x1, y1), (x2, y2))
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == 0 and r1 != r2:
        print(0)
    elif distance > r1 + r2:
        print(0)
    elif distance == r1 + r2:
        print(1)
    elif distance < r1 + r2 and distance > abs(r1 - r2):
        print(2)
    elif distance == abs(r1 - r2):
        print(1)
    elif distance < abs(r1 - r2):
        print(0)
        
        