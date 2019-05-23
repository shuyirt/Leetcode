class Solution:
    def rob(self, nums: List[int]) -> int:
        # earn E at house k:
        # E(k) = E(k-1) or E(k-2) + nums(k)
        # we just need to record 3 variable

        pre_house = 0
        cur_house = 0
        next_house = 0
        for num in nums:
            next_house = max(cur_house, pre_house + num)
            pre_house = cur_house
            cur_house = next_house
        return next_house