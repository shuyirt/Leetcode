# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.to_delete_set = set(to_delete)
        self.res = []

        self.dfs(root, True)
        return self.res
    
    def dfs(self, current_node, is_parent_deleted):
        if not current_node: 
            return None
        
        need_delete = current_node.val in self.to_delete_set
        
        if is_parent_deleted and not need_delete:
            self.res.append(current_node)

        current_node.left = self.dfs(current_node.left, need_delete)
        current_node.right = self.dfs(current_node.right, need_delete)
        
        return None if need_delete else current_node

Runtime: 64 ms, faster than 43.82% of Python online submissions for Delete Nodes And Return Forest.
Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Delete Nodes And Return Forest.
method: dfs + recursion