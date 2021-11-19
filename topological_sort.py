from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        stack = []
        if self.V == 1:
            stack = list(self.graph.keys())
            return stack
