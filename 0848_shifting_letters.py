class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        c = sum(shifts)
        r = []
        for i, x in enumerate(shifts):
            index = (ord(S[i])-97+c)%26+97
            c -= x
            r.append(chr(index))
        return "".join(r)

# Runtime: 80 ms, faster than 92.90% of Python3 online submissions for Shifting Letters.
# Memory Usage: 15.4 MB, less than 35.53% of Python3 online submissions for Shifting Letters.