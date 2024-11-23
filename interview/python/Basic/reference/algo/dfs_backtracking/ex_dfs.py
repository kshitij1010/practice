# Depth First Search or DFS for a Graph
#
# Reference:
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/


from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return

    def DFS_util(self, v, visited):
        visited.add(v)
        print (v, end=" ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFS_util(i, visited)

    def DFS(self, v):
        # set will keep track of visited vertex or node
        visited = set()

        # calling DFS utility function
        self.DFS_util(v, visited)

        # just to give a new line in output
        print ()
        return


# Example 1
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3, 3)
print ("Following is DFS from (starting from vertex 2):")
g1.DFS(2)


# Example 2
g2 = Graph()
g2.add_edge("a", "b")
g2.add_edge("a", "c")
g2.add_edge("b", "c")
g2.add_edge("c", "a")
g2.add_edge("c", "d")
print ("\nFollowing is DFS from (starting from vertex \"a\"):")
g2.DFS("a")


# Example 3
g3 = Graph()
g3.add_edge(1, 2)
g3.add_edge(1, 3)
g3.add_edge(2, 1)
g3.add_edge(2, 4)
g3.add_edge(2, 5)
g3.add_edge(3, 1)
g3.add_edge(3, 5)
g3.add_edge(4, 2)
g3.add_edge(4, 5)
g3.add_edge(4, 6)
g3.add_edge(5, 4)
g3.add_edge(5, 6)
print ("\nFollowing is DFS from (starting from vertex 1):")
g3.DFS(1)
