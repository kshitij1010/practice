# Example of merge_sort
#
# Time complexity: O(Nlog(N))
# Auxiliary Space: O(N)
# Algorithmic Paradigm: Divide and Conquer



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return


arr = [12, 11, 13, 5, 6, 7]
print (arr)
merge_sort(arr)
print (arr)
