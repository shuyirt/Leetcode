# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        flag = p.val == q.val
        right = self.isSameTree(p.right, q.right)
        left = self.isSameTree(p.left, q.left)
        return right and left and flag

# Runtime: 52 ms, faster than 23.99% of Python3 online submissions for Same Tree.
# Memory Usage: 13.8 MB, less than 75.42% of Python3 online submissions for Same Tree.
# method: recursion