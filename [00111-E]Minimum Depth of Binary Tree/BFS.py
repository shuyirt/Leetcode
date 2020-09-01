# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth
        level = [root]
        

        # BFS
        while level:
            depth += 1
            queue = []
            
            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue
        return depth

# Runtime: 44 ms, faster than 80.78% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 14.8 MB, less than 95.55% of Python3 online submissions for Minimum Depth of Binary Tree.
# method: BFS+list