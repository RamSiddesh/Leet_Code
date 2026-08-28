class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def subsets(start,obj):

            res.append(obj[:])

            
            for i in range(start,len(nums)):
                
                if i>start and nums[i] == nums[i-1]:
                    continue
                    
                obj.append(nums[i])
                subsets(i+1,obj)
                obj.pop()

            return res

        return subsets(0,[])