import InsertionSort

def bucketSort(tabl):
    temp = tabl
    
    largest = max(tabl)
    size = len(tabl)
    bucketSize = largest/size           # Difference between buckets
 
    buckets = [[] for i in range(size)] # Creates 51(size) undefined tables

    
    for i in range(0, size):
        j = int(tabl[i]/bucketSize)
        if j != size:
            buckets[j].append(tabl[i])
        else:
            buckets[size - 1].append(tabl[i])

    index = 0
 
    for i in range(0, size):
        InsertionSort.insertionSort(buckets[i])
        
        for j in range(0, len(buckets[i])):
            temp[index] = buckets[i][j]
            index += 1

    return temp