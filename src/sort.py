def partition(array, low, high, key):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # compare each element with pivot
    for j in range(low, high):
        if key(array[j]) <= key(pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
 
    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]
 
    # Return the position from where partition is done
    return i + 1

def quickSort(array, low, high, key=lambda x: x):
    if low < high:
        pi = partition(array, low, high, key)
        quickSort(array, low, pi - 1, key)
        quickSort(array, pi + 1, high, key)

if __name__ == "__main__":
    arr = [[3, 2], [1, 5], [6, 4], [2, 7]]

    quickSort(arr, 0, len(arr)-1, key=lambda x: x[0])
    print(arr)

    quickSort(arr, 0, len(arr)-1, key=lambda x: x[1])
    print(arr)
