# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t2:
            return t1
        if not t1:
            return t2
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Runtime: 84 ms, faster than 97.13% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.9 MB, less than 65.87% of Python3 online submissions for Merge Two Binary Trees.
# method: recursion 