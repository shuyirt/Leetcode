class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = []
        cur = n
        while cur != 1:
            cur = sum([int(i)**2 for i in str(cur) ])
            if cur in store:
                return False
            else:
                store.append(cur)
        return True

# Runtime: 28 ms, faster than 90.94% of Python3 online submissions for Happy Number.
# Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Happy Number.
# method: hashmap