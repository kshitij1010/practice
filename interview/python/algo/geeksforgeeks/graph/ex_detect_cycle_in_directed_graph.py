# Find if given directed graph has a cycle or not
#
# Reference:
# https://www.youtube.com/watch?v=rGaJgYS456c

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS_util(self, s, visited, visiting):
        visiting.add(s)
        for i in self.graph[s]:
            if i in visiting:
                return True
            if i not in visited:
                if self.DFS_util(i, visited, visiting):
                    return True
        visiting.remove(s)
        visited.add(s)
        return False

    def if_cycle(self):
        visited = set()
        visiting = set()
        for i in list(self.graph):
                if self.DFS_util(i, visited, visiting):
                    return True
        return False


# Example 1 # cycle at (2, 0) and (0, 2)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2) ####
g.add_edge(1, 2)
g.add_edge(2, 0) ####
g.add_edge(2, 3)
g.add_edge(3, 3)
print ("If cycle in the graph 1:", g.if_cycle(), "\n")


# Example 2 # no cycle
# a -> b, a -> c, b -> d, c -> d
g2 = Graph()
g2.add_edge("a", "b")
g2.add_edge("a", "c")
g2.add_edge("b", "d")
g2.add_edge("c", "d")
print ("If cycle in the graph 2:", g2.if_cycle(), "\n")

# Example 2.1 # Cycle in abcd -> abcd -> abcd
# a -> b, b -> d, d -> c, c -> a
g21 = Graph()
g21.add_edge("a", "b")
g21.add_edge("b", "d")
g21.add_edge("d", "c")
g21.add_edge("c", "a")
print ("If cycle in the graph 2.1:", g21.if_cycle(), "\n")

# Example 2.1 # Cycle in a -> bdc -> bdc -> bdc
# a -> b, b -> d, d -> c, c -> b
g22 = Graph()
g22.add_edge("a", "b")
g22.add_edge("b", "d")
g22.add_edge("d", "c")
g22.add_edge("c", "b")
print ("If cycle in the graph 2.2:", g22.if_cycle(), "\n")


# Example 3 # cycle at (0, 1) and (1, 0)
g3 = Graph()
g3.add_edge(0, 1) ###
g3.add_edge(1, 0) ###
g3.add_edge(2, 0)
g3.add_edge(3, 1)
g3.add_edge(3, 2)
g3.add_edge(4, 3)
print ("If cycle in the graph 3:", g3.if_cycle(), "\n")
