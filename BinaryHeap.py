# Max Heap
class maxHeap(object):

    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self,val):
        self.heaplist.append(val)
        self.size += 1
        return self.floatUp()

    def floatUp(self):
        nlist = self.size
        iparent = nlist//2
        icurrent = nlist
        while iparent > 0:
            if self.heaplist[iparent] < self.heaplist[icurrent]:
                self.heaplist[iparent],self.heaplist[icurrent] = \
                        self.heaplist[icurrent],self.heaplist[iparent]
                icurrent = iparent
                iparent = icurrent//2
            return True
        return True

    def pop(self):
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        return self.floatDown()

    def floatDown(self):
        nlist = self.size
        icurrent = 1
        while icurrent*2 <= nlist:
            ic2 = icurrent*2
            imax = self.minChild(ic2)
            if self.heaplist[imax] > self.heaplist[icurrent]:
                self.heaplist[imax],self.heaplist[icurrent]=\
                    self.heaplist[icurrent],self.heaplist[imax]
            icurrent = ic2
        return True

    def minChild(self,ic2):
        if ic2+1 > self.size:
                return ic2
        else:
            if self.heaplist[ic2]>self.heaplist[ic2+1]:
                return ic2
            else:
                return ic2+1 

    def printHeap(self):
        print(self.heaplist)

    def peek(self):
        return self.heaplist[1]
        





maxheap = maxHeap()
print(maxheap.insert(5))
print(maxheap.insert(77))
print(maxheap.insert(21))
maxheap.printHeap()
print(maxheap.insert(19))
print(maxheap.insert(20))
print(maxheap.insert(40))
maxheap.printHeap()
print(maxheap.pop())
maxheap.printHeap()
print(maxheap.peek())
