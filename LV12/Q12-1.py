N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
    
def bubble_sort(l):
    tmp_list = l[:]
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if tmp_list[j] > tmp_list[j + 1]:
                tmp = tmp_list[j]
                tmp_list[j] = tmp_list[j + 1]
                tmp_list[j + 1] = tmp
    return tmp_list

for num in bubble_sort(ls):
    print(num)
