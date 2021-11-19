N, M = map(int, input().split())
ls = []
for i in range(N):
    ls.append(input())
min_ = N * M
cnt = 0
for i in range(N - 7):
    for j in range(M - 7):
        for m in range(8):
            for n in range(8):
                s = ls[i + m][j + n]
                if (m + n) % 2 == 0:
                    if s == 'W':
                        cnt += 1
                else:
                    if s == 'B':
                        cnt += 1
        if cnt < min_:
            min_ = cnt
        cnt = 0
            
for i in range(N - 7):
    for j in range(M - 7):
        for m in range(8):
            for n in range(8):
                s = ls[i + m][j + n]
                if (m + n) % 2 == 0:
                    if s == 'B':
                        cnt += 1
                else:
                    if s == 'W':
                        cnt += 1
        if cnt < min_:
            min_ = cnt
        cnt = 0

print(min_)