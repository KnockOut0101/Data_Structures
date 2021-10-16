import numpy as np

class Linked_list:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data


def Create_Linked_list(size):
    nodes_array = np.array([])
    for i in range(size):
        data = int(input("Enter Data:-"))
        Node_variable = Node(data)
        nodes_array = np.append(nodes_array,Node_variable)

    Linked_list_start = Linked_list()
    Linked_list_start.head = nodes_array[0]
    for i in range(size):
        if (i == size-1):
            nodes_array[i].next = None
        else:
            nodes_array[i].next = nodes_array[i+1]

    return Linked_list_start,nodes_array

def Print_Linked_list(start,nodes):
    next = start.head
    for i in range(len(nodes)):
        print(next.data)
        next = nodes[i].next



Start,Nodes = Create_Linked_list(3)


Print_Linked_list(Start, Nodes)