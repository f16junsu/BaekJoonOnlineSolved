def ifhansu(num):
    num_str = str(num)
    if len(num_str) < 3:
        return True
    
    if int(num_str[0]) + int(num_str[2]) == 2 * int(num_str[1]):
        return True
    
    return False

N = int(input())
cnt = 0
for i in range(1, N + 1):
    if ifhansu(i):
        cnt += 1
        
print(cnt)