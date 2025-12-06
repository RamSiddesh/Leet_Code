1class Solution(object):
2    def twoSum(self, nums, target):
3        n=len(nums)
4        for i in range(n):
5            for j in range(n):              
6                if i != j:
7                    if nums[i]+nums[j] == target:
8                        return [i,j]
9
10        