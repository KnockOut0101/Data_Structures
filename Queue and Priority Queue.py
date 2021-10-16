'''  Written and Completed By Kshitij Ohri   '''



import numpy as np


def array_insert(a,b):
    a = np.append(a,b)
    return a


def array_pop(a):
    if (len(a) == 0):
        return(print("Stack is empty"))
    else:
        b=a[-1]
        a=a[:-1]
        return a,b


class Queue:
    def __init__(self):
        self.s1 =np.array([])
        self.s2 =np.array([])

    def enQueue(self, x):
        self.s1 = np.append(self.s1,x)
        print(self.s1)

    def deQueue(self):
            if (len(self.s1)==0 and len(self.s2)==0):
                print("Queue is Empty")
            elif(len(self.s1)>0 and len(self.s2)==0):
                while(len(self.s1)):
                    self.s1,temp = array_pop(self.s1)
                    self.s2 = array_insert(self.s2,temp)
                    #print(self.s2)
                self.s2,pop = array_pop(self.s2)
                return pop
            else:
                self.s2,pop = array_pop(self.s2)
                return pop

class PQueue:
    def __init__(self):
        self.s1 =np.array([]).astype(int)
        self.s2 =np.array([]).astype(int)

    def enQueue(self, x):
        self.s1 = np.append(self.s1,x)
        print(self.s1)

    def deQueue(self):
            if (len(self.s1)==0 and len(self.s2)==0):
                print("Queue is Empty")
            elif(len(self.s1)>0 and len(self.s2)==0):
                sort = np.array([])
                largest_no = 0
                index = 0
                for i in range(len(self.s1)):
                    if(self.s1[i]>largest_no):
                        largest_no = self.s1[i]
                        index = i
                self.s1 = np.delete(self.s1,index)
                self.s2 = np.append(self.s2,largest_no)
                self.s2,pop = array_pop(self.s2)
                sort = np.sort(self.s1, axis = 0)
                return pop,sort

            else:
                self.s2,pop = array_pop(self.s2)
                return pop


q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())

Q = PQueue()
Q.enQueue(int(1))
Q.enQueue(int(5))
Q.enQueue(int(7))
Q.enQueue(int(2))

a,b = Q.deQueue()
print(a,b)
a,b = Q.deQueue()
print(a,b)
a,b = Q.deQueue()
print(a,b)
a,b = Q.deQueue()
print(a,b)
