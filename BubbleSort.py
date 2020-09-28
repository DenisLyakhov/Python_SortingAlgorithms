def swap(tabl, i, j):
    tabl[i], tabl[j] = tabl[j], tabl[i]

def bubbleSort(tabl):
    temp = tabl
    
    found = -1

    while(found < 0):
        found = 0
        for i in range(1, len(temp)):
            if(temp[i-1]>temp[i]):
                swap(temp, i-1, i)
                found -= 1
    return temp