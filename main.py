import Sorting

if __name__ == '__main__':
    randArr=[31, 25, 11, 84, 5, 101]
    sortArr=Sorting.SelectionSort(randArr)
    sortArr=Sorting.BubbleSort(randArr)
    sortArr=Sorting.InsertionSort(randArr)
    sortArr=Sorting.MergeSort(randArr)
    print(sortArr)