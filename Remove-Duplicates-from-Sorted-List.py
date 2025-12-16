1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        dummy = ListNode('inf')
9        current = dummy
10        while head:
11            if current.val == head.val:
12                head = head.next
13                continue
14            current.next = head
15            current = current.next
16            head = head.next
17        current.next = None
18        return dummy.next
19
20
21
22        