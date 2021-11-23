# Selection Sort
def SelectionSort(ls):
    for i in range(len(ls)):
        min_ = (ls[i], i)
        for j in range(i, len(ls)):
            if ls[j] <= min_[0]:
                min_ = ls[j], j
        ls[i], ls[min_[1]] = min_[0], ls[i]
            
# Double Selection Sort
def DoubleSelectionSort(ls):
    i, j = (0, len(ls) - 1)
    while i < j:
        min_ = (ls[i], i)
        max_ = (ls[j], j)
        for k in range(i, j + 1):
            if ls[k] <= min_[0]:
                min_ = ls[k], k
            if ls[k] > max_[0]:
                max_ = ls[k], k
        ls[i], ls[min_[1]] = min_[0], ls[i]
        ls[j], ls[max_[1]] = max_[0], ls[j]
        i += 1; j -= 1
                
            
             
        
        
        
        
        
########## Test Cases ###########
ls = [-9, -6, -17, -9, 12, -18, 1, 1, 13, 4, -13, -18, -5, -12, 2, 20, 2, 5, -2, 3, 10, 6, 5, -3, 8, 9, -17, 5, 7, -8, 18, -4, 3, -11, 17, -3, 14, -2, -16, -6, -17, 3, 0, -9, 17, 6, 6, 5, -11, 11, -3, 9, 13, 0, 17, -18, -19, -12, 5, 10]
DoubleSelectionSort(ls)
print(ls)