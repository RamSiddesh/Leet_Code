1class Solution(object):
2    def strStr(self, haystack, needle):
3        n = len(haystack)
4        m = len(needle)
5        for i in range(n-m+1):
6            if haystack[i:i+m] == needle:
7                return i
8        return -1
9