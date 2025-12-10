1class Solution(object):
2    def removeElement(self, nums, val):
3        n = len(nums)
4        for i in range(n-1,-1,-1):
5            if nums[i] == val:
6                nums.remove(nums[i])
7            
8        