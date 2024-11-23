# Example of quick_sort
#
# Time complexity best/avg case: O(Nlog(N))
# Time complexity worst case: O(N^2)
# Space complexity: O(1)


def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left;


def quick_sort(arr, left, right):
    if left < right:
        pivot = arr[(left+right)//2]
        part = partition(arr, left, right, pivot)

        quick_sort(arr, left, part-1)
        quick_sort(arr, part, right)
    return


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)

print (arr)
