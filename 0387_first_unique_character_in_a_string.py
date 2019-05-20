class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        index = 0
        for index, i in enumerate(s):
            if count[i] == 1:
                return index
        return -1
