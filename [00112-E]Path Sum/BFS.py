# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        
        level = [[root, 0]]
        

        # BFS
        while level:
            queue = []
            
            for [node, value] in level:
                if not node.left and not node.right and node.val+value==sum:
                    return True
                if node.left:
                    queue.append([node.left, node.val+value])
                if node.right:
                    queue.append([node.right, node.val+value])
            level = queue
        return False

# Runtime: 32 ms, faster than 99.47% of Python3 online submissions for Path Sum.
# Memory Usage: 15.6 MB, less than 53.53% of Python3 online submissions for Path Sum.
# method: bfs+list