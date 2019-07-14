# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, lower, upper):
        if not node:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        return self.helper(node.left, lower,node.val) and self.helper(node.right, node.val,upper)

    # Runtime: 40 ms, faster than 99.57% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.7 MB, less than 56.65% of Python3 online submissions for Validate Binary Search Tree.