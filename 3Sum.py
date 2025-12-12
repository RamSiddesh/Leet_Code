1class Solution(object):
2    def threeSum(self, nums):
3        triplets = []
4        n = len(nums)
5        nums.sort()
6        total = 0
7        for i in range(n):
8            if i>0 and nums[i] == nums[i-1]:
9                continue
10            left = i+1
11            right = n-1
12            while left<right:
13                total=nums[i]+nums[left]+nums[right]
14                if total == 0:
15                    triplets.append([nums[i],nums[left],nums[right]])
16                    left+=1
17                    right-=1
18                    while left<right and nums[left]==nums[left-1]:
19                        left+=1
20                    while left<right and nums[right]==nums[right+1]:
21                        right-=1
22                elif total < 0:
23                    left+=1
24                elif total > 0:
25                    right-=1
26        return triplets