def SelectionSort(arr,reverse=False):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(reverse):
                if arr[min]<arr[j]:
                    min=j
            else:
                if arr[min]>arr[j]:
                    min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

def BubbleSort(arr,reverse=False):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(reverse):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def InsertionSort(arr,reverse=False):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        if(reverse):
            while(j>=0 and arr[j]<current):
                arr[j+1]=arr[j]
                j-=1
        else:
            while(j>=0 and arr[j]>current):
                arr[j+1]=arr[j]
                j-=1
        arr[j+1]=current
    return arr