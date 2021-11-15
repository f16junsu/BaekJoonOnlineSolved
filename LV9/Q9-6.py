def gold_partitions(num):
    ls = [False, False] + [True] * (num - 1)
    for i in range(2, int(num**.5) + 1):
        if ls[i]:
            for j in range(2 * i, num + 1, i):
                ls[j] = False
    primes = []
    for i in range(num + 1):
        if ls[i]:
            primes.append(i)
    partitions = []
    func = lambda x, y: (x, y) if x <= y else (y, x)
    for n in primes:
        if primes.count(num - n):
            t = func(n, num - n)
            if t in partitions:
                continue
            else:
                partitions.append(t)
    return partitions

T = int(input())
for i in range(T):
    num = int(input())
    partitions = gold_partitions(num)
    m, n = partitions[-1]
    print(m, n)
    
    #이놈의 시간초과 개빡치네