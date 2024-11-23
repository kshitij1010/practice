# 302. Route between Nodes
#
# Given a directed graph, design an algorithm to find out whether there is a route between two node.

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return

    # using BFS
    def if_path_exist(self, s, target):
        if s == target:
            return True
        visited = set()
        queue = []

        visited.add(s)
        queue.append(s)

        while queue:
            s = queue.pop(0)
            if s == target:
                return True

            for i in self.graph[s]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        if s == target:
            return True

        return False



# Example 1
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3, 3)
print ("\nIf path from \"1\" to \"3\" exist:")
print (g1.if_path_exist(1, 1))



# Example 2
g2 = Graph()
g2.add_edge("a", "b")
g2.add_edge("a", "c")
g2.add_edge("b", "c")
g2.add_edge("c", "a")
g2.add_edge("c", "d")
print ("\nIf path from \"a\" to \"b\" exist:")
print (g2.if_path_exist("a", "c"))
