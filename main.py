import Sorting

if __name__ == '__main__':
    randArr=[31, 25, 11, 84, 5, -2, 101, 33, -100]
    sortArr=Sorting.SelectionSort(randArr)
    sortArr=Sorting.BubbleSort(randArr)
    sortArr=Sorting.InsertionSort(randArr)
    sortArr=Sorting.MergeSort(randArr)
    sortArr=Sorting.QuickSort(randArr,0,len(randArr)-1)
    sortArr=Sorting.HeapSort(randArr)
    sortArr=Sorting.CountSort(randArr)
    sortArr=Sorting.RadixSort(randArr)
    sortArr=Sorting.ShellSort(randArr)
    print(sortArr)