class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = 0;
        for i in range (len(nums)):
            if nums[i] and nums[x]:
                x += 1
            elif nums[i]:
                nums[x] = nums[i]
                nums[i] = 0
                x += 1
        return nums

# Runtime: 32 ms, faster than 99.09% of Python online submissions for Move Zeroes.
# Memory Usage: 12.9 MB, less than 10.20% of Python online submissions for Move Zeroes.