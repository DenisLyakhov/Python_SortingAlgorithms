import random
import math

import BubbleSort
import SelectionSort
import InsertionSort
import QuickSort
import MergeSort
import HeapSort
import BucketSort


def init(tabl, size):
    random.seed()
    for i in range(0, size):
        tabl.append(random.randrange(100))
        
        
tabl = [30]
init(tabl, 30)

print(tabl)

print("Selection sort: \n")
temp = SelectionSort.selectionSort(tabl)
print(temp)
print("\n\n")

print("Insertion sort: \n")
temp = InsertionSort.insertionSort(tabl)
print(temp)
print("\n\n")

print("Bubble sort: \n")
temp = BubbleSort.bubbleSort(tabl)
print(temp)
print("\n\n")

print("Quick sort: \n")
temp = QuickSort.quickSort(tabl)
print(temp)
print("\n\n")

print("Merge sort: \n")
temp = MergeSort.mergeSort(tabl)
print(temp)
print("\n\n")

print("Heap sort: \n")
temp = HeapSort.heapSort(tabl)
print(temp)
print("\n\n")

print("Bucket sort: \n")
temp = BucketSort.bucketSort(tabl)
print(temp)
print("\n\n")