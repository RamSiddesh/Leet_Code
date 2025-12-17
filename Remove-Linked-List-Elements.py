1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def removeElements(self, head, val):
8        dummy = ListNode("inf")
9        cur = dummy
10        while head:
11            if head.val == val:
12                head = head.next
13            else:
14                cur.next = head
15                cur = cur.next
16                head = head.next
17        cur.next = None     
18        return dummy.next
19        