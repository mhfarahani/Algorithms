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


# Merge Sort:
# O(nlogn)
def mergeSort(alist):
    if len(alist)< 2:
        return alist
    else:
        isplit = len(alist)//2
        leftlist = mergeSort(alist[:isplit])
        rightlist = mergeSort(alist[isplit:])
        
        ileft = iright = ilist = 0
        while ileft < len(leftlist) and iright < len(rightlist):
            if leftlist[ileft] < rightlist[iright]:
                alist[ilist] = leftlist[ileft]
                ileft += 1
            else:
                alist[ilist] = rightlist[iright]
                iright += 1
            ilist += 1

        while ileft < len(leftlist):
            alist[ilist] = leftlist[ileft]
            ileft += 1
            ilist += 1
        while iright < len(rightlist):
             alist[ilist]=rightlist[iright]
             iright += 1
             ilist += 1
    return alist


# Quick Sort
# O(nlogn) to O(n^2)
def quickSort(alist):
    if len(alist) < 2:
        return alist
    else:
        ipivit = findPivit(alist)
        if ipivit != 0:
            alist[ipivit],alist[0] = alist[0],alist[ipivit]
            ipivit = 0
        left_list = quickSort([x for x in alist[1:] if x<=alist[0]])
        right_list = quickSort([x for x in alist[1:] if x>alist[0]])
        return left_list +[alist[0]]+ right_list

def findPivit(alist):
    imid = len(alist)//2
    if alist[0] > alist[-1]:
        if alist[0] > alist[imid]:
            return imid
        else:
            return 0
    elif alist[-1] > alist[imid]:
        return imid
    else:
        return -1
    

alist = [54,26,93,17,77,31,44,55,20]
print(quickSort(alist))
