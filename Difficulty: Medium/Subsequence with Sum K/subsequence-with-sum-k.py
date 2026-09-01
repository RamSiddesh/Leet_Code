class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        
        def subsets(i,total):
            if total > k:
                return False
            if i == len(arr):
                return total == k
            
            if subsets(i+1,total + arr[i]):
                return True
            
            if subsets(i+1,total):
                return True
                
            return False
            
        return subsets(0,0)
