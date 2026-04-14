"""Tests for the navigation graph, loader, and undo flow."""

import unittest
from pathlib import Path

from src.features.navigation import NavigationManager
from src.io.repositories import CampusDataRepository
from src.structures.graph import Graph


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


class GraphTests(unittest.TestCase):
    """Verify shortest-path behavior for the adjacency-list graph."""

    def test_shortest_path_prefers_lowest_cost_route(self) -> None:
        graph = Graph()
        graph.add_edge("ENG", "ENC", 2)
        graph.add_edge("ENC", "MSC", 4)
        graph.add_edge("ENG", "MSC", 8)
        graph.add_edge("MSC", "ST", 4)

        path, cost = graph.shortest_path("ENG", "ST")

        self.assertEqual(["ENG", "ENC", "MSC", "ST"], path)
        self.assertEqual(10, cost)

    def test_shortest_path_raises_for_unknown_destination(self) -> None:
        graph = Graph()
        graph.add_node("ENG")

        with self.assertRaises(ValueError):
            graph.shortest_path("ENG", "ST")


class NavigationIntegrationTests(unittest.TestCase):
    """Verify repository-backed navigation and undo history."""

    def test_repository_loads_navigation_graph_from_files(self) -> None:
        repository = CampusDataRepository(DATA_DIR)
        buildings = repository.load_buildings()
        graph = repository.load_navigation_graph()

        self.assertGreaterEqual(len(buildings), 7)
        self.assertEqual("Engineering Building", buildings[0].name)
        self.assertEqual(
            (["ENG", "ENC", "MSC", "ST"], 10),
            graph.shortest_path("ENG", "ST"),
        )

    def test_undo_restores_previous_route(self) -> None:
        repository = CampusDataRepository(DATA_DIR)
        manager = NavigationManager(repository.load_navigation_graph())

        first_route = manager.navigate("ENG", "ST")
        second_route = manager.navigate("EEEL", "ST")
        undo_message = manager.undo()

        self.assertEqual((["ENG", "ENC", "MSC", "ST"], 10), first_route)
        self.assertEqual((["EEEL", "TFDL", "ST"], 9), second_route)
        self.assertIsNotNone(undo_message)
        self.assertIn("Restored previous route", undo_message)


if __name__ == "__main__":
    unittest.main()
