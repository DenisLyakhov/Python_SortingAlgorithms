def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def merge(left,right):
    temp = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1


    for a in range(i, len(left)):
        temp.append(left[a])
    for a in range(j, len(right)):
        temp.append(right[a])
	
    return temp


def mergeSort(tabl):
    if(len(tabl) <= 1):
        return tabl
    mid = int(len(tabl)/2)
    left = mergeSort(tabl[:mid])
    right = mergeSort(tabl[mid:])

    return merge(left, right)