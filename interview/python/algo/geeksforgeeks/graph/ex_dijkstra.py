from collections import defaultdict
import time

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dijkstra_algo(self, src):
        # time complexity is O((v+e) log v)
        dist = dict()
        parent = dict()

        for vertex in self.graph.keys():
            dist[vertex] = float('inf')
            parent[vertex] = None

        dist[src] = 0
        unvisited = self.graph.copy()

        while unvisited:
            curr_vertex = None
            # Pick the minimum distance vertex from the set of vertices not yet processed
            # curr_vertex is always equal to src in the first iteration
            for vertex in unvisited:
                if curr_vertex == None:
                    curr_vertex = vertex
                elif dist[vertex] < dist[curr_vertex]:
                    curr_vertex = vertex

            # Update dist value of the adjacent vertices of the picked vertex only
            # if the current distance is greater than new distance and the vertex in not in the shotest path tree
            for vertex, weight in self.graph[curr_vertex]:
                if weight + dist[curr_vertex] < dist[vertex]:
                    dist[vertex] = weight + dist[curr_vertex]
                    parent[vertex] = curr_vertex

            unvisited.pop(curr_vertex)

        return dist, parent

    def find_shortest_path(self, start, end):
        d, p = self.dijkstra_algo(start)

        cur = end
        path = []
        while cur:
            path.append(cur)
            cur = p[cur]

        print (path[::-1])
        return path[::-1]


################## Example - 1
g= Graph()
g.add_edge(1, (2,10))
g.add_edge(1, (3,1))

g.add_edge(2, (4,2))

g.add_edge(3, (2,4))
g.add_edge(3, (4,8))
g.add_edge(3, (5,2))

g.add_edge(4, (5,7))
g.add_edge(5, (4,9))

print ("Example-1:")
# generate the dictionary with the distance to the each node from the start-node
print (g.dijkstra_algo(1)[0])
# shortest path(lowest weight of the path) to get from 1, 4
g.find_shortest_path(1, 4)
# {1: 0, 2: 5, 3: 1, 4: 7, 5: 3}

# time complexity with Adjacency List and Priority queue:
# O((v+e) log v)
# in worst case: e>>v so O( e log v)


################## Example - 2
graph_mat = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

g2 = Graph()

for i in range(len(graph_mat)):
    for j in range(len(graph_mat[0])):
        if graph_mat[i][j]:
            g2.add_edge(i, (j, graph_mat[i][j]))

# print (g2.graph)
print ("\n\nExample-2:")
print (g2.dijkstra_algo(0)[0])
# {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}

# time complexity with matrix and Priority queue:
# O(v^2 + e log v)
# in Worst case e ~ v^2
# Still based on this code example after creating Adjacency list from the matrix time complexity would be O((v+e) log v)
