from collections import defaultdict, deque


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return

    def DFS_util(self, v, visited, stack):
        visited.add(v)

        for s in self.graph[v]:
            if s not in visited:
                self.DFS_util(s, visited, stack)

        stack.insert(0,v)
        return


    def topological_sort(self):
        visited = set()
        stack = []
        for i in list(self.graph):
            if i not in visited:
                self.DFS_util(i, visited, stack)
        print (stack)


g= Graph()
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);

g.topological_sort() # [4, 5, 0, 2, 3, 1]
