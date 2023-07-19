from collections import defaultdict as dd

class Graph:

    def __init__(self):


        self.graph = dd(list)


    def addEdge(self, x, y):
        self.graph[x].append(y)



    def BFSearch(self, n):

        visited = (len(self.graph)) * [False]

        queue = []

        visited[n] = True
        queue.append(n)

        while queue:

            n = queue.pop(0)
            print(n, end=" ")

            for v in self.graph[n]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 1)
graph.addEdge(2, 2)
graph.addEdge(3, 1)
graph.addEdge(4, 3)
graph.addEdge(5, 4)

print(" The Breadth First Search Traversal for The Graph :s ")
graph.BFSearch(3)