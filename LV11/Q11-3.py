def bigger (tupA, tupB):
    if tupA[0] > tupB[0] and tupA[1] > tupB[1]:
        return -1
    elif tupA[0] < tupB[0] and tupA[1] < tupB[1]:
        return 1
    else:
        return 0
    
N = int(input())
ls = []
x, y = 0, 0

for i in range(N):
    x, y = map(int, input().split())
    ls.append((x, y))
grades = [0 for i in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if bigger(ls[i], ls[j]) == -1:
            grades[j] += 1
        elif bigger(ls[i], ls[j]) == 0:
            continue
        else:
            grades[i] += 1

for i in grades:
    print(i + 1, end=" ")