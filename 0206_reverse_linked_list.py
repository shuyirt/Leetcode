# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: notes.md
        :rtype: notes.md
        """

        # iterative
        # change the cur node's next to pre node
        # Ø   1 → 2 → 3 → Ø
        # Ø ← 1 ← 2 ← 3

        # cur = head
        # pre = None
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre

        # recursive method
        return self.helper(head)

    def helper(self, head):

        if head == None or head.next == None:
            return head
        else:
            # temp is the head of the reversed linked list
            temp = self.helper(head.next)

            # head is the upcoming node we need to reverse
            # node1 -> head -> B <- node2 <- node3 <- temp

            # we need to do: head -> B -> head
            head.next.next = head

            # and break the link from head -> B
            head.next = None

            return temp