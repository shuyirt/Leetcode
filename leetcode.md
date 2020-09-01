[TOC]



### Linked list

#### Remove Linked list node

##### 237. Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
```

##### 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value **val**.

```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # add a dummy head: always delete the next node
        a = ListNode(0)
        a.next = head
        temp = a
        temp_next = a
        
        while temp:
            temp_next = temp.next
            if temp_next and temp_next.val == val:
                temp.next = temp_next.next
                # del(temp_next)
            else:
                temp = temp.next
        head = a.next
        # del(a)
        return head
```

##### 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only *once*.

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            if node.next.val == node.val:
                node.next = node.next.next
                # del(node.next)
            else:
                node = node.next

        return head
```

##### 19. Remove Nth Node From End of List

Given a linked list, remove the *n*-th node from the end of list and return its head.

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = ListNode(0)
        a.next = head
        
        first = a
        second = a
        c = n+1
        
        while c:
            first = first.next
            c -= 1
        
        if c > 0:
            return head
        
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return a.next
```

#### traversal

##### 876. Middle of the Linked List

Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        first = second = head
        
        while first and first.next:
            second = second.next
            first = first.next.next
        return second
```

##### 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        
        return dummy.next
```



#### other

##### 1290. Convert Binary Number in a Linked List to Integer

```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        temp = head
        
        while temp != None:
            res = res *2 + temp.val 
            temp = temp.next
        return res
```

##### 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0);
        dummy.next = head.next;
        
        cur = head
        
        while cur and cur.next:
            # A B C D
            # B A D C

            c = cur.next.next
            
            # B -> A
            cur.next.next = cur

            if c and c.next:
                # A -> D if [A B C D]
                cur.next = c.next
            elif c and not c.next:
                # A -> C if [A B C]
                cur.next = c
                break
            else:
                # A -> None if [A B]
                cur.next = None
                break

            
            cur = c
        
        return dummy.next
```

