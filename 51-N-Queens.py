class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        comb = []

        col = set()
        pos_diagonal = set()
        neg_diagonal = set()

        def backtrack(r):
            if r == n:
                res.append(comb[:])
                return
            
            for c in range(n):
                if c in col or (r-c) in neg_diagonal or (r+c) in pos_diagonal:
                    continue

                col.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)

                comb.append("."*c + "Q" + "."*(n-c-1))

                backtrack(r+1)

                col.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                comb.pop()

        backtrack(0)
        return res