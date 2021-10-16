import numpy as np

'''Stack Implementation using numpy arrays'''

class Stack:
    def __init__(self, size):
        self.size = size
        self.Stack = np.array([])
    
    def push(self,data):
        if (len(self.Stack)<self.size):
            self.Stack = np.append(self.Stack,data)
            return print(self.Stack)
        else:
            return print("Stack is full"), self.Stack

    def array_pop(self):
        if (len(self.Stack) == 0):
            return(print("Stack is empty"))
        else:
            a=self.Stack[-1]
            self.Stack=self.Stack[:-1]
            return print(self.Stack,a)

    def print_Stack(self):
        return print(self.Stack)


Stack_array = Stack(5)

for i in range(5):
    Stack_array.push(i)

Stack_array.print_Stack()

for i in range(5):
    Stack_array.array_pop()

Stack_array.print_Stack()

