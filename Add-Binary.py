1class Solution(object):
2    def addBinary(self, a, b):
3        output = []
4        i = len(a) - 1
5        j = len(b) - 1
6        carry = 0
7
8        while i>=0 or j>=0 or carry:
9            bit_a = a[i] if i>=0 else '0'
10            bit_b = b[j] if j>=0 else '0'
11            ones = carry
12            if bit_a == '1':
13                ones+=1
14            if bit_b == '1':
15                ones+=1
16            
17            if ones%2 == 0:
18                output.append("0")
19            else: 
20                output.append("1")
21
22            if ones >=2:
23                carry = 1
24            else:
25                carry = 0
26
27            i -= 1
28            j -= 1
29
30        return ''.join(output[::-1])
31