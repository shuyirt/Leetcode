class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        while (num):
            print(num)
            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            elif num == 1:
                return True
            else:
                return False
        return True

# Runtime: 28 ms, faster than 77.42% of Python3 online submissions for Ugly Number.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Ugly Number.
# method: iteration