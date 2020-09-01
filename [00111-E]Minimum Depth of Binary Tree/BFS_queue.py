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
        q = deque()
        q.append(root)
        while q:
            depth += 1
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth
                else:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        return depth

# method: BFS+queue