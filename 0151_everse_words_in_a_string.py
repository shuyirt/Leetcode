class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        strings = s.split(" ")[::-1]
        strings = list(filter(lambda string: string != '', strings))
        res = ' '.join(strings)
        return res
# Runtime: 24 ms, faster than 99.92% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 13.5 MB, less than 36.11% of Python3 online submissions for Reverse Words in a String.