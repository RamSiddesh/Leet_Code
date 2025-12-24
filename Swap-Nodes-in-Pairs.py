1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def swapPairs(self, head):
8        dummy = ListNode(0)
9        dummy.next = head
10        prev = dummy
11        while prev.next and prev.next.next:
12            first = prev.next
13            second = first.next
14            nextpair = second.next
15            prev.next = second
16            second.next = first
17            first.next = nextpair
18            prev = first
19        return dummy.next
20