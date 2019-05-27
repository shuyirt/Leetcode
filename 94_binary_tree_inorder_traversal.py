# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.inorder(root, output)

        return output

    def inorder(self, x: TreeNode, output: List[int]):
        if x is not None:
            self.inorder(x.left, output)
            output.append(x.val)
            self.inorder(x.right, output)

# Runtime: 32 ms, faster than 97.18% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.1 MB, less than 55.96% of Python3 online submissions for Binary Tree Inorder Traversal.