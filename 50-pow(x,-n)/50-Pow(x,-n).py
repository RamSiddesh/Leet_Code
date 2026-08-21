class Solution:
    def myPow(self, x: float, n: int) -> float:      
        def recPow(x,n):
            if n==0:
                return 1
            if n%2==0:
                return recPow(x*x,n//2)
            else:
                return x * recPow(x*x,(n-1)//2)
        if n>0:
            return recPow(x,n)
        else:
            return recPow(1/x,-n)
