"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node
        visited = set()
        to_visit = [node]
        visited.add(node.val)

        graph = dict()

        while to_visit:
            cur_node = to_visit.pop()
            neighbors = []
            for adj in cur_node.neighbors:
                # print("adj val:",adj.val)
                if adj.val not in graph:
                    new_neighbor = Node(adj.val)
                    graph[adj.val] = new_neighbor
                neighbors.append(graph[adj.val])
                
                if adj.val not in visited:
                    visited.add(adj.val)
                    to_visit.append(adj)
    
            if cur_node.val not in graph:
                new_node = Node(cur_node.val)
            else:
                new_node = graph[cur_node.val]
            new_node.neighbors = neighbors
            graph[cur_node.val] = new_node
        
        return graph[1]
