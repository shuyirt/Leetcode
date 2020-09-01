# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
            res += self.rangeSumBST(root.left, L, R)
            res += self.rangeSumBST(root.right, L, R)
        elif L > root.val:
            res += self.rangeSumBST(root.right, L, R)
        elif R < root.val:
            res += self.rangeSumBST(root.left, L, R)

        return res

# Runtime: 228 ms, faster than 90.44% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22 MB, less than 28.30% of Python3 online submissions for Range Sum of BST.
# method: recursive