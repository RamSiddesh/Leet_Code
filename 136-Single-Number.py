class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#       dup = {}
#       for i in nums:
#           if i in dup:
#                dup[i] += 1
#           else:
#               dup[i] = 1

#       for i in nums:
#           if dup[i] == 1:
#              return i
        res = 0
        for i in nums:
            res = res^i
        return res



            

