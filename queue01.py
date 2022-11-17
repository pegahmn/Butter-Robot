

class Queue:
    def __init__(self):
        self.nodes=[]
    
    def enqueue(self, n):
        self.nodes.insert(0, n)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else: return self.nodes.pop()
    
    def is_empty(self):
        return len(self.nodes)==0
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:return self.nodes[-1]