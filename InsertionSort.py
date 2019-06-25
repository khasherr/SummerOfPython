#Insert sort

def InsertionSort(arr):
    for counter in range(len(arr)-1):
        midIndex = counter;
        for j in range(counter +1, len(arr)-1):
            if arr[midIndex] > arr[]