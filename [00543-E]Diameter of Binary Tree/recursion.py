# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.node_length = set()
        self.compute_node(root)
        return max(self.node_length)
    
    def compute_node(self, node):
        if not node:
            self.node_length.add(0)
            return 0
        
        left = self.compute_node(node.left)
        if node.left:
            left += 1
        
        right = self.compute_node(node.right)
        if node.right:
            right += 1
        self.node_length.add(left+right)
        # print(node.val, left, right, self.node_length)

        return max(left, right)

Runtime: 68 ms, faster than 11.98% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15.5 MB, less than 75.86% of Python3 online submissions for Diameter of Binary Tree.
method: recursion +  set