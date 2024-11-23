# Reference:
# https://www.youtube.com/watch?v=eaYX0Ee0Kcg

from heapq import heapify, heappushpop, heappop, heappush


def find_distance(origin, point):
    orig_x = origin[0]
    orig_y = origin[1]
    x = point[0]
    y = point[1]
    return ((x-orig_x)**2 + (y-orig_y)**2)**0.5


def k_closest(origin, points, k):
    distance_arr = []
    heapify(distance_arr)

    for point in points:
        distance = find_distance(origin, point)

        if len(distance_arr) < k:
            heappush(distance_arr, (distance*-1, point))
        else:
            heappushpop(distance_arr, (distance*-1, point))

    res = []

    while distance_arr:
        res.append(heappop(distance_arr)[1])

    return res[::-1]


points = [(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]
print (k_closest((0,0), points, 2))
