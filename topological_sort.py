from collections import defaultdict


class SortException(Exception):
    pass


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.edges = 0

    # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_helper(self, stack, visited, i):
        for j in self.graph[i]:
            if i == j:
                continue
            if visited[j]:
                raise SortException("Loop Exists")
            else:
                visited[j] = True
                stack.append(j)
                self.topological_sort_helper(stack, visited, j)

    def topological_sort(self):
        stack = []
        visited = [False] * (self.V + 1)
        for i in range(1, self.V + 1):
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                self.topological_sort_helper(stack, visited, i)
        return stack
