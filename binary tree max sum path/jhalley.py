# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.currMax = root.val
        return max(self.helper(root), self.currMax)
        
    def helper(self, root):
        sumThroughNode = maxForkedSum = None
        if root.left == None and root.right == None:
            maxForkedSum = root.val
            sumThroughNode = root.val
        else:
            sumLeft = self.helper(root.left) if root.left else 0
            sumRight = self.helper(root.right) if root.right else 0
            maxForkedSum = max(root.val, root.val+sumLeft, root.val+sumRight)
            sumThroughNode = root.val+sumLeft+sumRight
        
        self.currMax = max(self.currMax, maxForkedSum, sumThroughNode)
            
        return maxForkedSum
