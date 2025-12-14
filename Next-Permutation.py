1class Solution(object):
2    def nextPermutation(self, nums):
3        n = len(nums)
4        j = n-2
5        while j>=0 and nums[j]>=nums[j+1]:
6            j-=1
7        
8        if j>=0:
9            k = n-1
10            while k>0 and nums[k]<=nums[j]:
11                k-=1
12
13            nums[k],nums[j]=nums[j],nums[k]
14
15        nums[j+1:] = reversed(nums[j+1:])
16
17
18
19        