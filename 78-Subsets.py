class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def create_subset(i,arr):
            if i == len(nums):
                res.append(arr)
                return 

            create_subset(i+1,arr+[nums[i]]) #take
            create_subset(i+1,arr) #don't take

        create_subset(0,[])
        return res