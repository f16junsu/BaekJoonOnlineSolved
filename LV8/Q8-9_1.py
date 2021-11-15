T = int(input())

def jumps(d, k):
    s = sum(range(1, k + 1))
    if d == 0:
        return 0
    elif k == 0:
        return 1 + jumps(d - 1, 1)
    elif s < d - (k + 1): # 최대로 갈 수 있는 경우
        return 1 + jumps(d - (k + 1), k + 1)  
    elif s == d - (k + 1): # 최대로 정확히 갈수 있는 경우
         return k + 1
    elif (s - k) < d - k: # 가운데 값으로 갈 수 있는 경우
        return 1 + jumps(d - k, k)
    elif (s - k) == d - k:
        return k
    else:
        return 1 + jumps(d - (k - 1), k - 1)
        
""" def jumps(d):
    n = 0
    k = 0
    while d:
        s = sum(range(1, k + 1))
        if k == 0:
            n += 1; d -= 1
            k += 1
        elif s < d - (k + 1):
            n += 1; d -= (k + 1)
            k += 1
        elif s == d - (k + 1):
             n += (k + 1); break
        elif s - k < d - k:
            n += 1; d -= k
        elif s - k == d - k:
            n += k; break
        else:
            n += 1; d -= (k - 1)
            k -= 1
    return n """
        
for i in range(T):
    x, y = map(int, input().split())
    print(jumps(y - x, 0))
