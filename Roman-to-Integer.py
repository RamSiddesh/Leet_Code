1class Solution(object):
2    def romanToInt(self, s):
3        values = {
4            "I":1,
5            "V":5,
6            "X":10,
7            "L":50,
8            "C":100,
9            "D":500,
10            "M":1000
11        }
12        sum1 = 0
13        for i in range(len(s)):
14            if i+1 < len(s) and values[s[i]]<values[s[i+1]]:
15                sum1 -= values[s[i]]
16            else:
17                sum1 += values[s[i]]
18        return sum1