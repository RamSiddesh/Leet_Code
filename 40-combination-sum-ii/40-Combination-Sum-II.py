class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combsum(start,comb,total):
            if total == target:
                res.append(comb[:])
                return 
            
            if total > target or start >= len(candidates):
                return

            for i in range(start,len(candidates)):

                if i>start and candidates[i] == candidates[i-1]:
                    continue

                comb.append(candidates[i])
                combsum(i+1,comb,total+candidates[i])
                comb.pop()
            return res
        
        return combsum(0, [], 0)
        