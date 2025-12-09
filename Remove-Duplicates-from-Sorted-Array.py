1class Solution(object):
2    def removeDuplicates(self, nums):
3        k=1
4        for i in range(1,len(nums)):
5            if nums[i] != nums[i-1]:
6                nums[k]=nums[i]
7                k+=1
8        return k
9                
10
11        
12        