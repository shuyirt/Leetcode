# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = [root] # track discovered node
        depth = [1]
        cur = -1 # to implement a queue
        
        # BFS
        while cur < len(nodes)-1:
            cur += 1
            if nodes[cur].left:
                nodes.append(nodes[cur].left)
                depth.append(depth[cur]+1)
            if nodes[cur].right:
                nodes.append(nodes[cur].right)
                depth.append(depth[cur]+1)
        return max(depth)
    