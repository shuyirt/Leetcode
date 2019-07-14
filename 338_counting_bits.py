class Solution:
    def countBits(self, num: int) -> List[int]:
#         0: 0
#         1: 1

#         2: 1 = 1+0
#         3: 2 = 1+1

#         4: 1 = 1+0
#         5: 2 = 1+1
#         6: 2 = 1+2
#         7: 3 = 1+3
        res = [0]
        i = 1
        count = 0
        while count < num:
            l = len(res)
            for i in range(l):
                res.append(1+res[i])
                count += 1
                if count >= num:
                    return res
            i <<= 1
        return res

# Runtime: 104 ms, faster than 97.26% of Python3 online submissions for Counting Bits.
# Memory Usage: 15.9 MB, less than 33.75% of Python3 online submissions for Counting Bits.