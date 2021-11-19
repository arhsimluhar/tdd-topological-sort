import pytest

from topological_sort import Graph
from topological_sort import SortException


def test_topological_zero_vertices():
    g = Graph(0)
    assert g.topological_sort() == []


def test_topological_sort_single_vertex():
    g = Graph(1)
    g.addEdge(1, 1)
    assert g.topological_sort() == [1]


def test_topological_sort_single_edge():
    g = Graph(2)
    g.addEdge(1, 2)
    assert g.topological_sort() == [1, 2]


def test_topological_sort_neighbour_points_back():
    g = Graph(2)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    with pytest.raises(SortException):
        g.topological_sort()


def test_topological_sort_forms_loop():
    g = Graph(3)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    with pytest.raises(SortException):
        g.topological_sort()


def test_topological_sort_single_node_with_mulitple_neighbours():
    g = Graph(3)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    ans = g.topological_sort()
    assert ans in [[1, 2, 3], [1, 3, 2]]


def test_topological_sort_single_node_with_mulitple_neighbours_2():
    g = Graph(4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)

    ans = g.topological_sort()
    assert ans in [[1, 2, 3, 4],
                   [1, 2, 4, 3],
                   [1, 3, 4, 2],
                   [1, 3, 2, 4],
                   [1, 4, 2, 3],
                   [1, 4, 3, 2],
                   ]


