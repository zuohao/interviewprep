# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def convertToGraph(node):
            if node.left is not None:
                graph[node.left].append(node)
                graph[node].append(node.left)
                convertToGraph(node.left)
            if node.right is not None:
                graph[node.right].append(node)
                graph[node].append(node.right)
                convertToGraph(node.right)
        
        def getNodesUpToK(node, k):
            if k == 0:
                ret.append(node.val)
            else:
                neighbors = graph[node]
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    else:
                        visited.add(neighbor)
                        getNodesUpToK(neighbor, k-1)
                
                
        # Convert Binary Tree to Graph
        graph = defaultdict(list)
        convertToGraph(root)
        #print graph
        
        # DFS on graph starting from target to find all nodes K distance away
        visited = set([target])
        ret = []
        getNodesUpToK(target, K)
        
        return ret
        
