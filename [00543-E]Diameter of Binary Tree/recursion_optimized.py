# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.node_length = 1
        self.compute_node(root)
        return self.node_length - 1
    
    def compute_node(self, node):
        if not node:
            return 0
        
        left = self.compute_node(node.left)
        right = self.compute_node(node.right)
        self.node_length = max(self.node_length, left + right + 1)
        # print(node.val, left, right, self.node_length)

        return max(left, right) + 1

# Runtime: 48 ms, faster than 34.49% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.4 MB, less than 93.10% of Python3 online submissions for Diameter of Binary Tree.
# method: recursion, space optimized