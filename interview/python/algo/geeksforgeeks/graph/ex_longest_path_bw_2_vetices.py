# Given an undirected graph. Find the max sum of the weight between any 2 vertices.
# We are given a map of cities connected with each other via cable lines such that
# there is no cycle between any two cities.
# We need to find the maximum length of cable between any two cities for given city map.
#
# Reference:
# https://www.geeksforgeeks.org/longest-path-between-any-pair-of-vertices/

from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return

    def DFS_util(self, v, curr_sum, mx, visited):
        visited.add(v)
        val = 0
        for s in self.graph[v]:
            if s[0] not in visited:
                val = curr_sum + s[1]
                self.DFS_util(s[0], val, mx, visited)
            mx[0] = max(mx[0], val)

    def find_max_sum_of_weight(self):
        mx = [float('-inf')]
        for v in list(self.graph):
            visited = set()
            self.DFS_util(v, 0, mx, visited)
        return mx[0]


g= Graph()
g.add_edge(1, (2,3))
g.add_edge(2, (1,3))
g.add_edge(2, (3,4))
g.add_edge(3, (2,4))
g.add_edge(2, (6,2))
g.add_edge(6, (2,2))
g.add_edge(6, (5,5))
g.add_edge(5, (6,5))
g.add_edge(6, (4,6))
g.add_edge(4, (6,6))

print (g.find_max_sum_of_weight()) # 12
