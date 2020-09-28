def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def quickSort(tabl):
    temp = tabl

    qSort(temp, 0, len(temp)-1)

    return temp

def qSort(tabl, start, end):
    pivot = tabl[int((start+end)/2)]
    i = start
    j = end

    while(i <= j):
        while(tabl[i] < pivot):
            i += 1
        while(tabl[j] > pivot):
            j -= 1
        if (i <= j):
            swap(tabl, i, j)
            i += 1
            j -= 1
    if(start < j):
        qSort(tabl, start, j)
    if(i < end):
        qSort(tabl, i, end)