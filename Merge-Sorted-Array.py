1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3
4        nums1[:] = nums1[:m]
5        nums1.extend(nums2)
6
7        nums1.sort()
8        