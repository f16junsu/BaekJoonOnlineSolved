while True:
    n = int(input())
    if not n:
        break
    table = [False, False] + [True] * (2 * n - 1)
    for i in range(2, int((2*n)**.5) + 1):
        if table[i]:
            for j in range(2 * i, 2 * n + 1, i):
                table[j] = False
    print(table[n + 1:].count(True))