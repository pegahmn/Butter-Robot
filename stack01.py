
class Stack:
    def __init__(self):
        self.nodes=[]

    def push(self, n):
        self.nodes.append(n)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else: return self.nodes[-1]

    def is_empty(self):
        return len(self.nodes)==0
        

    