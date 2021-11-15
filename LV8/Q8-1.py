A, B, C = map(int, input().split())

# A + Bn <= Cn
# A / (C - B) <= n

if (C - B) <= 0:
    print(-1)
else:
    print(A // (C - B) + 1)