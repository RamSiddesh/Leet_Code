1class Solution(object):
2    def threeSumClosest(self, nums, target):
3        best = float('inf')
4        n = len(nums)
5        nums.sort()
6        for i in range(n):
7            l = i+1
8            r = n-1
9            while l<r:
10                sum1 = nums[i]+nums[l]+nums[r]
11                if abs(sum1-target) < abs(best-target):
12                    best=sum1
13                if sum1 < target:
14                    l+=1
15                elif sum1 > target:
16                    r-=1
17                else:
18                    return sum1
19        return best
20                
21
22
23
24
25
26        