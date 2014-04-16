from django.test import TestCase

from problems import graph


class GraphTestCase(TestCase):
	def test_one(self):
		"""
		Tests the Graph's capability to order its nodes (1).
		"""
		g = graph.Graph({
			'A': [],
			'B': ['A'],
			'C': [],
			'D': ['C'],
			'E': ['A'],
			'F': ['D', 'E', 'G'],
			'G': []
		})
		self.assertEqual(g.get_ordered_nodes(), [
			{'A', 'C', 'G'},
			{'B', 'E', 'D'},
			{'F', }
		])
	
	def test_two(self):
		"""
		Tests the Graph's capability to order its nodes (2).
		"""
		g = graph.Graph({
			'A': [],
			'B': ['A'],
			'C': ['B'],
			'D': ['B'],
			'E': ['C'],
			'F': ['C', 'D'],
			'G': ['D']
		})
		self.assertEqual(g.get_ordered_nodes(), [
			{'A', },
			{'B', },
			{'C', 'D'},
			{'E', 'F', 'G'},
		])

