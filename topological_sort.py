from collections import defaultdict


class SortException(Exception):
    pass


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_helper(self, stack, visited, neighbors, i):
        visited[i] = True
        neighbors[i] = True
        for j in self.graph[i]:
            if not visited[j]:
                self.topological_sort_helper(stack, visited, neighbors, j)
            elif neighbors[j] and j != i:
                raise SortException
        stack.insert(0, i)
        neighbors[i] = False

    def topological_sort(self):
        stack = []
        visited = [False] * (self.V + 1)
        neighbors = [False] * (self.V + 1)
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.topological_sort_helper(stack, visited, neighbors, i)

        return stack
