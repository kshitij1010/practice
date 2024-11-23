# Example of heap_sort
#
# Overall Time complexity: O(Nlog(N))
# Time complexity for building the heap O(N)
# Space complexity: O(1)

import heapq

def heap_sort(arr):
    res = []
    heapq.heapify(arr)
    while len(arr) > 0:
        res.append(heapq.heappop(arr))
    return res

arr = [5, 7, 9, 1, 3]
print (heap_sort(arr))


'''
To create max_heap example,
elements = [5, 1, 3, 7, 2]

heapq._heapify_max(elements)
pop_max = heapq._heappop_max(elements)

print(pop_max)

'''
