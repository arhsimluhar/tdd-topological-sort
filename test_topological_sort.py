from topological_sort import Graph


def test_topological_sort_single_vertex():
    g = Graph(1)
    g.addEdge(1, 1)
    assert g.topological_sort() == [1]


def test_topological_sort_single_edge():
    g = Graph(2)
    g.addEdge(1,2)
    assert g.topological_sort() == [1, 2]
