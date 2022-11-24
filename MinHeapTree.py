class MHT:
    def __init__(self):
        self.A = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

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

    def swap(self, indx1, indx2):
        temp = self.A[indx1]
        self.A[indx1] = self.A[indx2]
        self.A[indx2] = temp

    def push(self, node):
        self.A.append(node)
        self.size += 1
        self.heapifyup(self.size-1)

    def heapifyup(self, index):
        if(self.hasParent(index) and self.parent(index) > self.A[index]):
            self.swap(self.getParentIndx(index), index)
            self.heapifyup(self.getParentIndx(index))

    def pop(self):
        if self.is_empty():
            raise Exception('Empty heap')
        node = self.A[0]
        self.A[0] = self.A.pop()
        self.size -= 1
        self.heapifydown(0)
        return node

    def heapifydown(self, index):
        smallest = index
        if(self.hasLeftchild(index) and self.A[smallest] > self.leftchild[index]):
            smallest = self.getLeftchild(index)

        if(self.hasRightchild(index) and self.A[smallest] > self.rightchild[index]):
            smallest = self.getRightchild(index)

        if(smallest != index):
            self.swap(index, smallest)
            self.heapifydown(smallest)

    def print(self):
        print(self.A)
