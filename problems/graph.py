class Graph:
	def __init__(self, structure):
		"""
		Constructor.
		"""
		self.structure = structure
	
	def get_predecessors(self, node):
		"""
		Returns list of nodes that are predecessors of the given node.
		"""
		if node in self.structure:
			return self.structure[node]
		else:
			return None
	
	def get_ordered_nodes(self):
		"""
		Returns all nodes, ordered.
		"""
		levels = []
		remaining_nodes = list(self.structure.keys())
		while remaining_nodes:
			current_level = set()
			new_remaining_nodes = list(remaining_nodes)
			for node in remaining_nodes:
				for predecessor in self.structure[node]:
					if predecessor in remaining_nodes:
						break
				else:
					current_level.add(node)
					new_remaining_nodes.remove(node)
			levels.append(current_level)
			remaining_nodes = new_remaining_nodes
		return levels

