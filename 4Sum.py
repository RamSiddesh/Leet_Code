1class Solution(object):
2    def fourSum(self, nums, target):
3        n = len(nums)
4        sums=0
5        op_list = []
6        nums.sort()
7        for i in range(n-3):
8            if i>0 and nums[i]==nums[i-1]:
9                continue
10            for j in range(i+1,n-2):
11                if j>i+1 and nums[j]==nums[j-1]:
12                    continue
13                l=j+1
14                r=n-1
15                while l<r:
16                    sums = nums[i]+nums[j]+nums[l]+nums[r]
17                    if sums<target:
18                        l+=1
19                    elif sums>target:
20                        r-=1
21                    else:
22                        op_list.append([nums[i],nums[j],nums[l],nums[r]])
23                        l+=1
24                        r-=1
25                        while l<r and nums[l]==nums[l-1]:
26                            l+=1
27                        while l<r and nums[r]==nums[r+1]:
28                            r-=1
29        return op_list
30
31
32        