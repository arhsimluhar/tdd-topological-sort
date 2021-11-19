from topological_sort import Graph


def test_topological_sort_single_vertex():
    g = Graph(1)
    g.addEdge(1, 1)
    assert g.topological_sort() == [1]