1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def addTwoNumbers(self, l1, l2):
8        digit = 0
9        carry = 0
10        dummy = ListNode(0)
11        cur = dummy
12        while l1 and l2:
13            sum1 = l1.val + l2.val + carry
14            digit = sum1 % 10
15            carry = sum1 // 10
16            new_node = ListNode(digit)
17            cur.next = new_node
18            cur = cur.next
19            l1 = l1.next
20            l2 = l2.next
21
22        if l2 == None:
23            while l1:
24                sum1 = l1.val + carry
25                digit = sum1 % 10
26                carry = sum1 // 10
27                new_node = ListNode(digit)
28                cur.next = new_node
29                cur = cur.next
30                l1 = l1.next
31        elif l1 == None:
32
33            while l2:
34                sum1 = l2.val + carry
35                digit = sum1 % 10
36                carry = sum1 // 10
37                new_node = ListNode(digit)
38                cur.next = new_node
39                cur = cur.next
40                l2 = l2.next
41        if carry != 0:
42            new_node = ListNode(carry)
43            cur.next = new_node
44
45        return dummy.next
46        
47
48
49
50
51
52
53
54
55            
56        