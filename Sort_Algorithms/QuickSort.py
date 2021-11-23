# QuickSort with Cache
def QuickSort1(ls):
    if len(ls) <= 1:
        return ls
    else:
        smaller = []
        bigger = []
        equal = []
        pivot = ls[len(ls) // 2]
        for i in ls:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                bigger.append(i)
            else:
                equal.append(i)
        return QuickSort1(smaller) + equal + QuickSort1(bigger)
    
# QuickSort without Cache
def QuickSort2(ls, start, end):
    if start >= end:
        return
    else:
        pivot = ls[end]
        i = start
        j = end - 1
        while i < j:
            if ls[i] >= pivot and ls[j] <= pivot:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1; j -= 1
            elif ls[i] >= pivot and ls[j] > pivot:
                j -= 1
            elif ls[i] < pivot and ls[j] > pivot:
                i += 1; j -= 1
            else:
                i += 1
        if ls[i] >= pivot:
            pass
        else:
            i += 1
        ls[i], ls[end] = ls[end], ls[i]
            
        QuickSort2(ls, start, i - 1)
        QuickSort2(ls, i + 1, end)
    
# QuickSort wiki version
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quick_sort(arr, start, end):
    if start < end:
        pivot_ind = partition(arr, start, end)
        quick_sort(arr, start, pivot_ind - 1)
        quick_sort(arr, pivot_ind + 1, end)
    return arr






########## Test Cases ########
ls = [-9, -6, -17, -9, 12, -18, 1, 1, 13, 4, -13, -18, -5, -12, 2, 20, 2, 5, -2, 3, 10, 6, 5, -3, 8, 9, -17, 5, 7, -8, 18, -4, 3, -11, 17, -3, 14, -2, -16, -6, -17, 3, 0, -9, 17, 6, 6, 5, -11, 11, -3, 9, 13, 0, 17, -18, -19, -12, 5, 10]
ls1 = ls[:]
print(QuickSort1(ls))
QuickSort2(ls, 0, len(ls) - 1)
print(ls)
quick_sort(ls1, 0, len(ls1) - 1)
print(ls1)