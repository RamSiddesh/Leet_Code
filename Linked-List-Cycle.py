1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def hasCycle(self, head):
9        fast = head
10        slow = head
11        while fast and fast.next:
12            fast = fast.next.next
13            slow = slow.next
14            if fast == slow:
15                return True
16        return False