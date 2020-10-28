# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def calcNodeScores(node, depth, node_score):
            node_scores_at_depth[depth].append(node_score)
            if node.left:
                calcNodeScores(node.left, depth+1, node_score*2)
            if node.right:
                calcNodeScores(node.right, depth+1, node_score*2+1)
        
        
        node_scores_at_depth = defaultdict(list) 
        calcNodeScores(root, 0, 0)
        
        ret = 0
        for depth in node_scores_at_depth.keys():
            max_at_depth = max(node_scores_at_depth[depth])
            min_at_depth = min(node_scores_at_depth[depth])
            ret = max(ret, max_at_depth - min_at_depth + 1)
                
        return ret
