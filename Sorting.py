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
 
def HeapSort(arr,reverse=False):
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

def CountSort(arr,reverse=False):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    if(reverse):
        arr=arr[::-1]
    return arr

def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def RadixSort(arr,reverse=False):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10
    if(reverse):
        arr=arr[::-1]
    return arr

def ShellSort(arr,reverse=False):
    gap = len(arr) // 2 # initialize the gap
 
    while gap > 0:
        i = 0
        j = gap
         
        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):
     
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
         
            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:
 
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
 
        gap //= 2
    if(reverse):
        arr=arr[::-1]
    return arr