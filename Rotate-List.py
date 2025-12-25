1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def rotateRight(self, head, k):
8        if (head and head.next) is None:
9            return head
10
11        ptr = head
12        length = 1
13        while ptr.next:
14            ptr = ptr.next
15            length+=1
16        
17        k %= length
18        if k == 0 :
19            return head
20        stop = length - k
21        
22
23        tail = head
24        for i in range(stop-1):
25            tail = tail.next
26
27        new_head = tail.next
28        tail.next = None
29        ptr.next = head
30        return new_head
31 
32
33
34
35
36
37        
38        