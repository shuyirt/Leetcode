class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # a = collections.Counter(i for i in s)
        # b = collections.Counter(i for i in t)
        # return a==b

        return sorted(s) == sorted(t)