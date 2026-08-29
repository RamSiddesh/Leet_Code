class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []  

        def getAllParts(s, parts):
            if len(s) == 0:
                ans.append(parts[:])  
                return
            for i in range(len(s)):
                part = s[:i + 1]
                if isPalindrome(part):
                    parts.append(part)
                    getAllParts(s[i + 1:],parts)
                    parts.pop() 

        def isPalindrome(s):
            return s == s[::-1]
            
        getAllParts(s,[])
        return ans
      