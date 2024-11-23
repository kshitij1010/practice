# BFS and DFS undirected graph

from collections import defaultdict, deque

class Graph:
    def __init__(self, ):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        if s is None:
            return

        visited = set()
        queue = deque([])

        visited.add(s)
        queue.append(s)

        while queue:
            s = queue.popleft()
            print (s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return

    def DFS_util(self, s, visited):
        visited.add(s)
        print (s, end=" ")

        for i in self.graph[s]:
            if i not in visited:
                self.DFS_util(i, visited)

    def DFS(self, s):
        visited = set()
        self.DFS_util(s, visited)


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
print ("\nFollowing is DFS from (starting from vertex 2):")
g1.DFS(2)
