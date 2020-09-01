# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root

# Runtime: 76 ms, faster than 87.20% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.8 MB, less than 49.47% of Python3 online submissions for Search in a Binary Search Tree.
# method: recursion