# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from notes import ListNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = l1
        y = l2
        l3 = ListNode(0)
        z = l3
        ''' 
        case 1: (2 -> 4 )     + (5 -> 6 -> 4)  = (7 -> 0 -> 5)
        case 2: (2 -> 4 -> 3) + (5 -> 6 )      = (7 -> 0 -> 4)
        case 3: (2 -> 4 -> 3) + (5 -> 6 -> 4)  = (7 -> 0 -> 8)
        case 4: (2 -> 4 -> 7) + (5 -> 6 -> 4)  = (7 -> 0 -> 2 -> 1)
        '''
        carry = 0
        while x or y:
            x_val = 0 if x == None else x.val
            y_val = 0 if y == None else y.val

            value = x_val + y_val + carry
            carry = value // 10
            value = value % 10

            x = x.next if x else None
            y = y.next if y else None

            # print(x_val,'+', y_val, '=', carry, '|', value)

            z.val = value
            if (x or y or carry):
                z.next = ListNode(carry)
                z = z.next

        return l3

# Runtime: 76 ms, faster than 98.16% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.4 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.

