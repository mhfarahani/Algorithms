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

# Shell Sort
# O(n^1.5) to O(n^2)

def shellSort(alist):
    lenght = len(alist)
    gap = lenght //2 
    while gap > 0:
        for i in range(lenght-gap):
            j = i+gap
            while j > gap-1 and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j]=alist[j],alist[j-gap]
                j -= gap
        gap = gap//2
    return alist
                
import pdb

# Merge Sort:
# O(nlogn)
def mergeSort(alist):
    if len(alist)< 2:
        return alist
    else:
        pdb.set_trace()
        isplit = len(alist)//2
        print(len(alist),isplit)
        leftlist = mergeSort(alist[:isplit])
        rightlist = mergeSort(alist[isplit:])
        
        ileft = iright = 0
        while ileft < len(leftlist)-1 and iright < len(rightright)-1:
            if leftlist[ileft] < rightlist[iright]:
                alist[i] = leftlist[ileft]
                ileft += 1
            else:
                alist[i] = rightlist[iright]
                iright += 1
        else:
            if ileft != len(leftlist)-1:
                alist.append(leftlist[ileft:])
            else:
                alist.append(rightlist[iright:])
                
        return alist

    


alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(alist))
