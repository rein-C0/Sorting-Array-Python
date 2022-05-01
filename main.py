import Sorting

if __name__ == '__main__':
    randArr=[31, 25, 11, 84, 5, 101, 33]
    sortArr=Sorting.SelectionSort(randArr)
    sortArr=Sorting.BubbleSort(randArr)
    sortArr=Sorting.InsertionSort(randArr)
    sortArr=Sorting.MergeSort(randArr)
    sortArr=Sorting.QuickSort(randArr,0,len(randArr)-1)
    sortArr=Sorting.heapSort(randArr)
    print(sortArr)