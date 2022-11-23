

class MHT:
    def __init__(self, capacity):
        self.A = []*capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndx(self, indx):
        return(indx-1)//2

    def getLeftchild(self, indx):
        return (indx*2)+1

    def getRightchild(self, indx):
        return(indx*2)+2

    def hasParent(self, indx):
        return self.getParentIndx(indx) >= 0

    def hasRightchild(self, indx):
        return self.getRightchild(indx) < self.size

    def hasLeftchild(self, indx):
        return self.getLeftchild(indx) < self.size

    def parent(self, indx):
        return self.A[self.getParentIndx(indx)]

    def leftchild(self, indx):
        return self.A[self.getLeftchild(indx)]

    def rightchild(self, indx):
        return self.A[self.getRightchild(indx)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, indx1, indx2):
        temp = self.A[indx1]
        self.A[indx1] = self.A[indx2]
        self.A[indx2] = temp

    def insert(self, node):
        if(self.isFull()):
            raise('Heap is full.')
        else:
            self.A[self.size] = node
            self.size += 1
            self.heapifyup(self.size-1)

    def heapifyup(self, index):
        if(self.hasParent(index) and self.parent(index) > self.A[index]):
            self.swap(self.getParentIndx(index), index)
            index = self.getParentIndx(index)

    def removeMin(self):
        if(self.size == 0):
            raise('Empty heap')
        node = self.A[0]
        self.A[0] = self.A[self.size-1]
        self.size -= 1
        self.heapifydown(0)
        return node

    def heapifydown(self, index):
        smallest = index
        if(self.hasLeftchild(index), self.A[smallest] > self.leftchild[index]):
            smallest = self.getLeftchild(index)

        if(self.hasRightchild(index) and self.A[smallest] > self.rightchild[index]):
            smallest = self.getRightchild(index)

        if(smallest != index):
            self.swap(index, smallest)
            self.heapifydown(smallest)

    def print(self):
        print(self.A)
