N = int(input())

def partition_sum(num):
    sum = num
    for c in str(num):
        sum += int(c)
    return sum

def find(num):
    for i in range(1, N):
        if partition_sum(i) == N:
            return i
    return 0

print(find(N))