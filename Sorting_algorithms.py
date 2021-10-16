import numpy as np


array = [4, 2, 3, 8, 8, 43, 6,1, 0]
'''size = int(input("Enter size of array:-"))

for i in range(size):
    data = int(input("Enter data:-"))
    array = np.append(array,data)'''

selection = int(input("Choose Sorting Algorithm:-"))

print("Original Array:-\n",array)

def Bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]
        print(array)

def Insertion_sort(array):
    for i in range(1,len(array)):
        j = i-1
        temp = array[i]
        while(j >=0 and temp < array[j]):
            array[j+1]=array[j]
            j-=1
            print(array)
        array[j+1] = temp
    print(array)

def heapify(array,size=len(array),index = 0):
    root = index
    left = 2*root+1
    right = 2*root+2

    if(left<size and array[root]<left):
        root = left
    
    if(right<size and array[root]<right):
        root = right
    
    if (root != index):
        array[index],array[root]=array[root],array[index]

        heapify(array,size,root)

def Heap_sort(array,size=len(array)):
    for i in range(size//2 - 1,-1,-1):
        heapify(array,size,i)
    for i in range(size-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)
    print(array)

def Merge(array, left_index, right_index, middle):
    
    left = array[left_index:middle + 1]
    right = array[middle+1:right_index+1]

    left_array_index = 0
    right_array_index = 0
    sorted_index = left_index

    while left_array_index < len(left) and right_array_index < len(right):
        if left[left_array_index] <= right[right_array_index]:
            array[sorted_index] = left[left_array_index]
            left_array_index = left_array_index + 1
        else:
            array[sorted_index] = right[right_array_index]
            right_array_index = right_array_index + 1

        sorted_index = sorted_index + 1

    while left_array_index < len(left):
        array[sorted_index] = left[left_array_index]
        left_array_index = left_array_index + 1
        sorted_index = sorted_index + 1

    while right_array_index < len(right):
        array[sorted_index] = right[right_array_index]
        right_array_index = right_array_index + 1
        sorted_index = sorted_index + 1
    

def Merge_sort(array, left_index=0, right_index = len(array)-1):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    Merge_sort(array, left_index, middle)
    Merge_sort(array, middle + 1, right_index)
    Merge(array, left_index, right_index, middle)
    return print(array)

def Sorting_algo(array,number):
    if(number == 1):
        print("Bubble Sort")
        Bubble_sort(array)
    elif(number == 2):
        print("Insertion Sort")
        Insertion_sort(array)
    elif(number == 3):
        print("Merge Sort")
        Merge_sort(array)
    elif(number == 4):
        print("Heap Sort")
        Heap_sort(array)
        
    
    

Sorting_algo(array,selection)
