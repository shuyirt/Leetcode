"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        queue = [head]
        pre = cur = None
        
        while len(queue):
            
            pre = cur
            cur = queue.pop()
            if pre and pre.child == cur:
                pre.next = cur
                cur.prev = pre
                pre.child = None
            elif cur.prev != pre:
                cur.prev = pre
                pre.next = cur
            if cur.next:
                queue.append(cur.next)
            if cur.child:
                queue.append(cur.child)
            
        return head
# Runtime: 32 ms, faster than 79.41% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# method: dfs