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
        def cloneNode(n):
            if node is None:
                return node
            if n.val in visited:
                return visited[n.val]
            
            clone = Node(n.val, None)
            visited[n.val] = clone
            clone.neighbors = [cloneNode(i) for i in n.neighbors]
            
            return clone
                
            
        visited  = {}
        return cloneNode(node)
    
        
