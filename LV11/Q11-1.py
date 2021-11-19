N, M = map(int, input().split())
ls = list(map(int, input().split()))

def find(l):
    diff = M
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                tmp = l[i] + l[j] + l[k]
                if tmp == M:
                    return M
                elif tmp < M:
                    if (M - tmp) < diff:
                        diff = M - tmp
    return M - diff

print(find(ls))