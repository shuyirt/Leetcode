class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        
        for i in range(len(nums)):
            if nums[x] and nums[i]:
                x += 1
            elif nums[i]:
                nums[x], nums[i] = nums[i], nums[x]
                x += 1

Runtime: 44 ms, faster than 90.85% of Python3 online submissions for Move Zeroes.
Memory Usage: 15 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
method: two pointer
All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
All elements between the current and slow pointer are zeroes.