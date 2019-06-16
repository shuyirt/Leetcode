class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        self.res = []
        self.backtrack(digits, '')
        return self.res

    def backtrack(self, digits, s):
        if len(digits) == 0:
            self.res.append(s)
        else:
            for a in self.mapping[digits[0]]:
                self.backtrack(digits[1:], s + a)

# Runtime: 36 ms, faster than 87.99% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.2 MB, less than 56.00% of Python3 online submissions for Letter Combinations of a Phone Number.