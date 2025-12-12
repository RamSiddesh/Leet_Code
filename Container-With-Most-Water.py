1class Solution(object):
2    def maxArea(self, height):
3        n= len(height)
4        left=0
5        right=n-1
6        width=0
7        max_area = 0
8        while left < right:
9            width = right-left
10            breadth = height[left] if height[left] <= height[right] else height[right]
11            if width*breadth > max_area:
12                max_area = width*breadth
13            if height[left]<height[right]:
14                left+=1
15                width-=1
16            else:
17                right-=1
18                width-=1
19        return max_area
20
21
22        