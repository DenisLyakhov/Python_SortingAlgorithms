def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def selectionSort(tabl):

    temp = tabl
    
    maxIndex = 0

    for i in range(0, len(temp)):
        maxIndex = i
        for j in range(i, len(temp)):
            if(temp[j] > temp[maxIndex]):
                maxIndex = j
        swap(temp, i, maxIndex)

    for i in range(0, int(len(temp)/2)):
        swap(temp, i, len(temp)-1-i)

    return temp