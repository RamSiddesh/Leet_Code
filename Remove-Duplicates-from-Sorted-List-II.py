1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        dummy = ListNode(0)
9        dummy.next = head
10        prev = dummy
11        ptr2 = head
12        while ptr2:
13            if ptr2.next and ptr2.val == ptr2.next.val:
14                dup = ptr2.val
15                while ptr2 and ptr2.val == dup:
16                    ptr2 = ptr2.next
17                prev.next = ptr2
18            else:
19                prev = ptr2
20                ptr2 = ptr2.next
21        return dummy.next
22
23        