#Using Dynamic programming

ls = [[0 for i in range(15)] for j in range(15)]
for i in range(1, 15):
    ls[0][i] = i
for i in range(15):
    ls[i][1] = 1
    
def numbers(k, n):
    global ls
    if ls[k][n]:
        return ls[k][n]
    else:
        su = sum([numbers(k - 1, i) for i in range(1, n + 1)])
        ls[k][n] = su
        return su

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(numbers(k, n))