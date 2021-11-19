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
        self.edges += 1

    def num_of_edges(self):
        return self.edges

    def topological_sort_helper(self, stack, visited, i):
        for j in self.graph[i]:
            if visited[j]:
                raise SortException("Loop Exists")
            else:
                visited[j] = True
                stack.append(j)
                self.topological_sort_helper(stack, visited, j)

    def topological_sort(self):
        stack = []
        visited = [False] * (self.V + 1)
        if self.V == 0:
            stack = []
        if self.V == 1:
            stack = list(self.graph.keys())
            return stack

        if self.num_of_edges() == 1:
            for i in self.graph:
                stack.append(i)
                stack.append(self.graph[i][0])
        else:
            for i in range(1, self.V):
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
                    self.topological_sort_helper(stack, visited, i)

                else:
                    return stack

        return stack
