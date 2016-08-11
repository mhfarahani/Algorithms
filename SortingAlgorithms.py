## Bubble Sort

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
            

alist = [54,26,93,17,77,31,44,55,20]
print(bubleSort(alist))
