from typing import Dict, AnyStr


class Graph():
    costs = {}
    parents = {}
    graph_dict = {}
    processed = []

    def __init__(self, graph_dict: Dict, beginning: AnyStr):
        self.graph_dict = graph_dict
        self.costs = self._get_initial_costs(graph_dict, beginning)
        self.parents = self._get_initial_parents(graph_dict, beginning)

    def _get_initial_costs(self, graph: Dict, beginning: AnyStr) -> Dict:
        costs = dict.fromkeys(graph.keys(), float('inf'))
        costs.update(graph.get(beginning))
        costs.pop(beginning)
        return costs

    def _get_initial_parents(self, graph: Dict, beginning: AnyStr) -> Dict:
        parents = dict.fromkeys(graph.keys(), None)
        for k, v in graph[beginning].items():
            parents[k] = beginning
        parents.pop(beginning)
        return parents

    def _find_lowest_cost_node(self) -> Dict:
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def count_shortest_path(self) -> Dict:
        node = self._find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph_dict[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self._find_lowest_cost_node()

        return {
            'costs': self.costs,
            'parents': self.parents
        }
