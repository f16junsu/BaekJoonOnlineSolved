# BubbleSort
def BubbleSort(l):
    tmp_list = l[:]
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if tmp_list[j] > tmp_list[j + 1]:
                tmp = tmp_list[j]
                tmp_list[j] = tmp_list[j + 1]
                tmp_list[j + 1] = tmp
    return tmp_list






########## Test Cases ###########
ls = [-9, -6, -17, -9, 12, -18, 1, 1, 13, 4, -13, -18, -5, -12, 2, 20, 2, 5, -2, 3, 10, 6, 5, -3, 8, 9, -17, 5, 7, -8, 18, -4, 3, -11, 17, -3, 14, -2, -16, -6, -17, 3, 0, -9, 17, 6, 6, 5, -11, 11, -3, 9, 13, 0, 17, -18, -19, -12, 5, 10]
print(BubbleSort(ls))