def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def insertionSort(tabl):
    temp = tabl

    for i in range(1, len(temp)):
        if(temp[i-1] > temp[i]):
            j = i
            while(temp[j] < temp[j-1] and j - 1 >= 0):
                swap(temp, j, j-1)
                j -= 1
    return temp