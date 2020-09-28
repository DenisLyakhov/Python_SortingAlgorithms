def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def heapSort(tabl):
    temp = tabl

    hSort(tabl)

    return temp

def hSort(tabl):
    end = len(tabl)

    for root in range(end, -1, -1):
        buildMaxHeap(tabl, end, root)
        
    for root in range(end-1, 0, -1):
        swap(tabl, root, 0)
        buildMaxHeap(tabl, root, 0)


def buildMaxHeap(tabl, end, root):
    left = 2*root
    right = 2*root + 1
    max = root

    if left < end and tabl[root] < tabl[left]:
        max = left
    if right < end and tabl[max] < tabl[right]:
        max = right

    if max != root:
        swap(tabl, root, max)
        buildMaxHeap(tabl, end, max)