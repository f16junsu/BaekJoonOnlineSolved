# MergeSort
def Merge(ls_a, ls_b):
    done = False
    lis = []
    while not done:
        if ls_a and ls_b:
            if ls_a[0] > ls_b[0]:
                lis.append(ls_b.pop(0))
            else:
                lis.append(ls_a.pop(0))
        elif ls_a and not ls_b:
            lis = lis + ls_a; break
        elif not ls_a and ls_b:
            lis = lis + ls_b; break
        else:
            break
    return lis
            
def MergeSort(ls):
    if len(ls) == 1:
        return ls
    else:
        left = ls[:len(ls) // 2]
        right = ls[len(ls) // 2:]
        return Merge(MergeSort(left), MergeSort(right))
        
        


########### Test Cases ############
ls = [-9, -6, -17, -9, 12, -18, 1, 1, 13, 4, -13, -18, -5, -12, 2, 20, 2, 5, -2, 3, 10, 6, 5, -3, 8, 9, -17, 5, 7, -8, 18, -4, 3, -11, 17, -3, 14, -2, -16, -6, -17, 3, 0, -9, 17, 6, 6, 5, -11, 11, -3, 9, 13, 0, 17, -18, -19, -12, 5, 10]
print(MergeSort(ls))