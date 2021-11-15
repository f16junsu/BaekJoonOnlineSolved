def gold_partitions(num):
    table = [False, False] + [True] * (num - 1)
    primes = []
    partitions = []
    for i in range(2, int(num**.5) + 1):
        if table[i]:
            for j in range(2 * i, num + 1, i):
                table[j] = False
    for i in range(num + 1):
        if table[i]:
            primes.append(i)
    partitions = []
    for n in primes:
        if n > num // 2:
            break
        if primes.count(num - n):
            partitions.append((n, num - n))
    return partitions

T = int(input())
for i in range(T):
    num = int(input())
    partitions = gold_partitions(num)
    m, n = partitions.pop()
    print(m, n)
