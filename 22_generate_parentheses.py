class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.res = []
        self.n = n
        self.backtrack("", 0, 0)

        return self.res

    def backtrack(self, s, a, b):
        if len(s) == 2 * self.n:
            self.res.append(s)
            return None

        if a < self.n:
            self.backtrack(s + "(", a + 1, b)

        if a > b:
            self.backtrack(s + ")", a, b + 1)


# Runtime: 48 ms, faster than 33.64% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 13.5 MB, less than 28.97% of Python3 online submissions for Generate Parentheses.
