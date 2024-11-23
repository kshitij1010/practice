# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

from heapq import heappop, heappush


def num_of_conference_room(arr):
    if len(arr) == 0 or arr is None:
        return 0

    arr = sorted(arr)

    h = []

    res = 0

    for i in arr:
        start, end = i

        if h and h[0] < start:
            heappop(h)

        heappush(h, end)

        res = max(res, len(h))

    return res


times = [[0, 30],[5, 10],[15, 20]]
print (num_of_conference_room(times)) # 2


times1 = [[0, 30],[5, 15],[15, 20]]
print (num_of_conference_room(times1)) # 3
