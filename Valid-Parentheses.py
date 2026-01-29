1class Solution(object):
2    def isValid(self, s):
3        dict1 = {
4            "}":"{",
5            "]":"[",
6            ")":"("
7        }
8        stack1 = []
9        for i in s:
10            if i in dict1.values():
11                stack1.append(i)      
12            else:
13                if not stack1 or stack1.pop() != dict1[i]:
14                    return False
15        return len(stack1)==0
16
17        