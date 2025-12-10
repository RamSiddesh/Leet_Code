1class Solution(object):
2    def plusOne(self, digits):
3        n=1
4        for i in range(len(digits)-1,-1,-1):
5            n+=digits[i]*(10**(len(digits)-i-1))
6        str1 = str(n)
7        digits[:]=[]
8        for i in range(len(str1)):
9            digits.append(int(str1[i]))          
10        return digits
11        