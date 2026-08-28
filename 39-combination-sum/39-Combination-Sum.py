class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combsum(start,comb,total):
            if sum(comb) == target:
                res.append(comb[:])
                return

            if total>target or start >= len(candidates):
                return
            
            comb.append(candidates[start])

            combsum(start,comb,total+candidates[start])

            comb.pop()
            combsum(start+1,comb,total)

            return res

        return combsum(0,[],0)


            


        