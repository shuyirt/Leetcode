# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        temp = root 
        while temp:
            if val > temp.val:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                else:
                    temp = temp.right
            else:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                else:
                    temp = temp.left
        return TreeNode(val)
        
        # Runtime: 124 ms, faster than 70.77% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15.4 MB, less than 57.43% of Python3 online submissions for Insert into a Binary Search Tree.