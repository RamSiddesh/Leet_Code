1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def removeNthFromEnd(self, head, n):
8        dummy = ListNode(0)
9        dummy.next = head
10        # we do this just to be able to delete the head node if necessary
11        # dummy -> head
12        ptr1 = dummy
13        ptr2 = dummy
14        for i in range(n+1):
15            ptr1 = ptr1.next
16        while ptr1:
17            ptr2 = ptr2.next
18            ptr1 = ptr1.next
19        ptr2.next = ptr2.next.next
20        return dummy.next
21        
22
23
24
25        
26
27        