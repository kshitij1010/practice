# Breadth First Search or BFS for a Graph
#
# Reference:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return

    def BFS(self, s):
        # set will keep track of visited vertex or node
        visited = set()
        # since we are starting from the "s" vertex, we are visiting s so we can make that visited
        visited.add(s)

        # queue for the visiting help
        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)
            print (s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        print () # just to give a new line in output
        return

# Example 1
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3, 3)
print ("Following is Breadth First Traversal (starting from vertex 2):")
g1.BFS(2)


# Example 2
g2 = Graph()
g2.add_edge("a", "b")
g2.add_edge("a", "c")
g2.add_edge("b", "c")
g2.add_edge("c", "a")
g2.add_edge("c", "d")
print ("\nFollowing is Breadth First Traversal (starting from vertex \"a\"):")
g2.BFS("a")


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
print ("\nFollowing is Breadth First Traversal (starting from vertex 1):")
g3.BFS(1)
