# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, node):
        if not node:
            return(0, float("-inf"))
        (left_sided_max,left_cur_max) = self.traverse(node.left)
        (right_sided_max,right_cur_max) = self.traverse(node.right)
        sided_max = max(left_sided_max, right_sided_max)+node.val
        cur_max = max([left_cur_max, right_cur_max, left_sided_max+right_sided_max+node.val])
        return (max(0,sided_max), cur_max)
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root)[1]
    
