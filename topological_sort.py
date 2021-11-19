from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.edges = 0

    # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.edges += 1

    def num_of_edges(self):
        return self.edges

    def topological_sort(self):
        stack = []
        if self.V == 1:
            stack = list(self.graph.keys())
            return stack

        if self.num_of_edges() == 1:
            for i in self.graph:
                stack.append(i)
                stack.append(self.graph[i][0])
            return stack
