class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()

        def combsum(s,comb,total):

            # result
            if total == target:
                res.append(comb[:])
                return 
            
            #more than target and if ran thru whole list
            if total > target or s >= len(candidates):
                return

            

            for i in range(s,len(candidates)):
                if i>s and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                combsum(i+1,comb+[candidates[i]],total+candidates[i])
            return res
        
        return combsum(0, [], 0)
        