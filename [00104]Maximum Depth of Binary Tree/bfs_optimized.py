# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        level = [root] if root else []
        depth = 0

        # BFS
        while level:
            depth += 1
            queue = []
            
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue
        return depth

# time: 36 ms O(n) -88%
# space: 13.9mb O(log(n))
# method: BFS optimized