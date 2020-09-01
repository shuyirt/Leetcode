class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for i in shift:
            direction, move = i
            if direction:
                total_shift -= move
            else:
                total_shift += move
        total_shift %= len(s)
        # print(total_shift, s, s[total_shift:], s[:total_shift])
        return s[total_shift:] + s[:total_shift]

# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.7 MB
# method: iterative + string
