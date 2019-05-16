class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for stone in S:
            count = count+1 if stone in J else count
        return count

'''
Runtime: 12 ms, faster than 99.74% of Python online submissions for Jewels and Stones.
Memory Usage: 11.7 MB, less than 78.26% of Python online submissions for Jewels and Stones.

'''


''' or this solution, using a hashset
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
'''