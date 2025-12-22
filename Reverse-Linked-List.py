1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseList(self, head):
8        cur = head
9        prev = None
10        while cur:
11            nex = cur.next
12            cur.next = prev
13            prev = cur
14            cur = nex
15        return prev
16            
17
18
19
20            
21
22
23
24        