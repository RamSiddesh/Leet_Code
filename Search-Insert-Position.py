1class Solution(object):
2    def searchInsert(self, nums, target):
3        n = len(nums)
4        for i in range(n):
5            if nums[i] == target:
6                return i
7            elif nums[i] > target and nums[i-1] < target:
8                return i
9        if target > nums[n-1]:
10            return n
11        elif target < nums[0]:
12            return 0
13            
14
15
16        