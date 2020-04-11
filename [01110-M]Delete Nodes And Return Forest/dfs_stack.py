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
        result = []
        if not root:
            return result
        

        dfs_queue = [root]
        while len(dfs_queue) != 0:
            # fetch the current node and append children
            current_node = dfs_queue.pop()
            if current_node.right:
                dfs_queue.append(current_node.right)
            if current_node.left:
                dfs_queue.append(current_node.left)

            # remove the connection if children need to be deleted
            if current_node.right and current_node.right.val in to_delete:
                current_node.right = None
            if current_node.left and current_node.left.val  in to_delete:
                current_node.left = None  
            
            
            # check if we need to remove the current node
            if current_node.val in to_delete:
                if current_node.right:
                    result.append(current_node.right)
                if current_node.left:
                    result.append(current_node.left)
                del(current_node)

        if root.val not in to_delete:
            result.append(root)

        return result

# Runtime: 84 ms, faster than 14.90% of Python online submissions for Delete Nodes And Return Forest.
# Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Delete Nodes And Return Forest.
# method: dfs + stack
