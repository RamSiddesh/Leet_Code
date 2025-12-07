1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        str1 = strs[0]
4        for i in strs[1:]:
5            while i.find(str1) !=0:
6                str1 = str1[:-1]
7                if not str1:
8                    return ""
9
10        return str1
11                
12
13
14        