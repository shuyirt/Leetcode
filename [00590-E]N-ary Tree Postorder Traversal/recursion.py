"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        res = []
        for child in root.children:
            res += self.postorder(child)
        return res + [root.val]


# Runtime: 56 ms, faster than 63.75% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 15.7 MB, less than 50.62% of Python3 online submissions for N-ary Tree Preorder Traversal.
# method: list + recursion