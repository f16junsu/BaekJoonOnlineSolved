T = int(input())

def jumps(d):
    ifeven = d % 2 == 0
    half = d // 2 
    k = 0
    while True:
        if k * (k + 1) // 2 < half:
            k += 1; continue
        elif k * (k + 1) // 2 == half and ifeven:
            return 2 * k
        elif k * (k + 1) // 2 == half and not ifeven:
            return 2 * k + 1
        elif d <= k ** 2:
            return 2 * k - 1
        else:
            return 2 * k
            
for i in range(T):
    x, y = map(int, input().split())
    print(jumps(y - x))
