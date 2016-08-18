## Bubble Sort
# O(n^2)
def bubleSort(alist):
    length = len(alist)
    for i in range(length):
        sorted_flag = True
        for j in range(length-i-1):
            if alist[j+1] < alist[j]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                sorted_flag = False
        if sorted_flag:
            return alist
    return alist

## Selection Sort
# O(n^2)
def selectionSort(alist):
    lenght = len(alist)
    for i in range(lenght):
        max_index = 0
        for j in range(1,lenght-i):
            if alist[max_index]<alist[j]:
                max_index = j
        if j != max_index:
            alist[j],alist[max_index]=alist[max_index],alist[j]
    return alist

# Insertion Sort
# O(n^2)
def insertionSort(alist):
    lenght = len(alist)
    for i in range(1,lenght):
        j = i
        while alist[j-1]>alist[j] and j > 0:
            alist[j],alist[j-1]=alist[j-1],alist[j]
            j -= 1
    return alist
            

alist = [54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))
