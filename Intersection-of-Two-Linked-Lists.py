1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def getIntersectionNode(self, headA, headB):
9        cur1 = headA
10        cur2 = headB
11        while cur1 != cur2:
12            if cur1 == None:
13                cur1 = headB
14            else:
15                cur1 = cur1.next 
16            if cur2 == None:
17                cur2 = headA
18            else:
19                cur2 = cur2.next
20        return cur1
21            
22
23
24
25        