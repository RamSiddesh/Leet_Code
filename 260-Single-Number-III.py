class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
#        dup = {}
#        for i in nums:
#            if i in dup:
#               dup[i] +=1
#            else:
#                dup[i] = 1
#        res = []
#        for i in dup:
#            if dup[i] == 1:
#                res.append(i)
#        return res
        xor = 0
        for i in nums:
            xor ^= i
        
        sep = 1
        while xor & sep == 0:
            sep = sep << 1
        
        a = 0
        b = 0
        for i in nums:
            if i & sep == 0:
                a ^= i
            else:
                b ^= i
        return [a,b]
