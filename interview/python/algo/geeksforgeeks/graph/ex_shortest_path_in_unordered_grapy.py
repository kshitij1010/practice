# You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.
#
# Given information about active users on the network,
# find the shortest route for a message from one user (the sender) to another (the recipient).
# Return a list of users that make up this route.
#
# Example,
# Input:  (Graph, start_node, end_node)
#         (network =   {
#                         'Min'     : ['William', 'Jayden', 'Omar'],
#                         'William' : ['Min', 'Noam'],
#                         'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
#                         'Ren'     : ['Jayden', 'Omar'],
#                         'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
#                         'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
#                         'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
#                         'Noam'    : ['Nathan', 'Jayden', 'William'],
#                         'Omar'    : ['Ren', 'Min', 'Scott'],
#                         ...
#                     },
#         Jayden,
#         Adams)
# Find the shortest path to send a message from Jayden to Adam
# Output: ['Jayden', 'Amelia', 'Adam']
#
# Reference:
# https://www.interviewcake.com/question/python/mesh-message?course=fc1&section=trees-graphs

from collections import deque

def find_shortest_path_helper(path_map, start_node, end_node):
    path = []

    curr = end_node

    while curr:
        path.append(curr)
        curr = path_map[curr]

    return path[::-1]


def bfs_get_path(graph, start_node, end_node):
    if start_node is None or end_node is None:
        return None

    path_map = {start_node: None}

    queue = deque([])
    queue.append(start_node)

    while len(queue) > 0:
        s = queue.popleft()

        if s == end_node:
            return find_shortest_path_helper(path_map, start_node, end_node)

        for i in graph[s]:
            if i not in path_map:
                path_map.update({i:s})
                queue.append(i)

    return None



graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }


print (bfs_get_path(graph, 'a', 'e')) # a, c, e
print (bfs_get_path(graph, 'a', 'a')) # a
print (bfs_get_path(graph, 'd', 'c')) # d, a, c
print (bfs_get_path(graph, 'f', 'g')) # f, g
print (bfs_get_path(graph, 'a', 'f')) # None
