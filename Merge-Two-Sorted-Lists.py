1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def mergeTwoLists(self, list1, list2):
8        dummy = ListNode(0)
9        curr = dummy
10        while list1 and list2:
11            if list1.val<list2.val:
12                curr.next = list1
13                list1 = list1.next
14                curr = curr.next
15            else:
16                curr.next = list2
17                list2 = list2.next
18                curr = curr.next
19        
20        curr.next = list1 or list2
21        return dummy.next
22            
23        