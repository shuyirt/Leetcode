# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Runtime O(N): 28 ms, faster than 61.37% of Python3 online submissions for Middle of the Linked List.
# Memory Usage O(1): 13.9 MB, less than 7.14% of Python3 online submissions for Middle of the Linked List.
# method: two pointer - slow fast pointer

# slower pointer move 1 step at a time
# fast pointer move 2 steps at a time