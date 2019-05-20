# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from notes import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: notes.md
        :type l2: notes.md
        :rtype: notes.md
        """
        x = l1
        y = l2
        l3 = ListNode(-1)
        z = l3

        '''
            case1: 1->2->4,  1->3->4
            case2: 1->2->4,  1->3
            case3: 1->2,     1->3->4
        '''

        while x and y:
            if (x.val <= y.val):
                z.next = x
                x = x.next
            else:
                z.next = y
                y = y.next
            z = z.next
        z.next = x if x else y

        return l3.next

# Runtime: 28 ms, faster than 70.74% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 11.8 MB, less than 5.04% of Python online submissions for Merge Two Sorted Lists.