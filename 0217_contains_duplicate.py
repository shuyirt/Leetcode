class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)

        for a in nums:
            if c[a] > 1:
                return True
        return False

# Runtime: 44 ms, faster than 91.09% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.3 MB, less than 5.12% of Python3 online submissions for Contains Duplicate.