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

def Partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low, high):
        if(arr[j]<=pivot):
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def QuickSort(arr,low,high,reverse=False):
    if(low<high):
        pi=Partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
    if(reverse):
        arr=arr[::-1]
    return arr

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr,reverse=False):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
    if(reverse):
        arr=arr[::-1]
    return arr