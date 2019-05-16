class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:]
        y = 0
        x = 0
        i = 0
        while x < m and y < n:
            if nums3[x] <= nums2[y]:
                nums1[i] = nums3[x]
                x += 1
            else:
                nums1[i] = nums2[y]
                y += 1
            i += 1

        if x < m:
            nums1[i:] = nums3[x:m]
        else:
            nums1[i:] = nums2[y:]
