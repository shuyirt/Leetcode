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