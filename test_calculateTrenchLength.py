import unittest
import networkx as nx
from main import calculateTrenchLength


class TestCalculateTrenchLength(unittest.TestCase):
    def setUp(self):
        # Create a graph with three nodes and two edges
        self.tree = nx.Graph()
        self.tree.add_edge(1, 2, length=5)
        self.tree.add_edge(2, 3, length=10)

    def test_same_nodes(self):
        # Test the case where the source and target nodes are the same
        length = calculateTrenchLength(self.tree, 1, 1)
        self.assertEqual(length, 0)

    def test_directly_connected(self):
        # Test the case where the source and target nodes are directly connected
        length = calculateTrenchLength(self.tree, 1, 2)
        self.assertEqual(length, 5)

    def test_indirectly_connected(self):
        # Test the case where the source and target nodes are indirectly connected
        length = calculateTrenchLength(self.tree, 1, 3)
        self.assertEqual(length, 15)

    def test_no_path(self):
        # Test the case where there is no path between the source and target nodes
        length = calculateTrenchLength(self.tree, 1, 2)
        self.assertIsNone(length)


