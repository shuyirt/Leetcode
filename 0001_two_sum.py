class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Given nums = [2, 7, 11, 15], target = 9

        # store {2:0, 7:1, 11:2, 15:3}
        table = {}
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[num] = i


# one pass hash table solution

''' tricky input
    1. [3,3] 6
    2. [3,2,4] 6
'''