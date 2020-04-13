# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.findPath(root, '')
    def findPath(self, node: TreeNode, path: str) -> List[str]:
        if not node: 
            return []
        node_path = "{}->{}".format(path, node.val) if path else str(node.val)
        if not node.right and not node.left:
            return [node_path]
        return self.findPath(node.left, node_path)  + self.findPath(node.right, node_path) 


# Runtime: 28 ms, faster than 83.67% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
# method: recursion