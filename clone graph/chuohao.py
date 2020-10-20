from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return node
        visited_node = {}
        visit_queue = deque()
        visit_queue.append(node)
        visited_node[node] = Node(node.val)
        while visit_queue:
            cur_node = visit_queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in visited_node:
                    visit_queue.append(neighbor)
                    visited_node[neighbor] = Node(neighbor.val)
                visited_node[cur_node].neighbors.append(visited_node[neighbor])
        return visited_node[node]
