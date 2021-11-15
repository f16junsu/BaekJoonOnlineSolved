def gold_partitions(num):
    table = [False, False] + [True] * (num - 1)
    partitions = ()
    for i in range(2, int(num**.5) + 1):
        if table[i]:
            for j in range(2 * i, num + 1, i):
                table[j] = False
    for i in range(2, num // 2 + 1):
        if table[i] and table[num - i]:
            partitions = (i, num - i)
    return partitions

T = int(input())
for i in range(T):
    num = int(input())
    print(*gold_partitions(num))