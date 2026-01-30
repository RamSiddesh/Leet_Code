1class Solution(object):
2    def lengthOfLastWord(self, s):
3        list1 = s.split()
4        return len(list1[len(list1)-1])
5        