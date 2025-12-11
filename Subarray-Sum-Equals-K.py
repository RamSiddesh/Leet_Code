1class Solution(object):
2    def subarraySum(self, nums, k):
3        res=0
4        curSum=0
5        prefixSums={0:1}
6
7        for i in nums:
8            curSum += i
9            diff = curSum - k
10
11            res += prefixSums.get(diff,0)
12            prefixSums[curSum] = 1+ prefixSums.get(curSum,0)
13        return res