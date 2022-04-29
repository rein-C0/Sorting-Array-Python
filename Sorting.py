def SelectionSort(arr,reverse=False):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    if(reverse):
        arr=arr[::-1]
    return arr

def BubbleSort(arr,reverse=False):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    if(reverse):
        arr=arr[::-1]
    return arr

def InsertionSort(arr,reverse=False):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while(j>=0 and arr[j]>current):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current
    if(reverse):
        arr=arr[::-1]
    return arr

def MergeSort(arr,reverse=False):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        MergeSort(L)
        # Sorting the second half
        MergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    if(reverse):
        arr=arr[::-1]
    return arr