class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 or N == 1:
            return N

        # list based
        # l = [0, 1]
        # for i in range(2, N+1):
        #     l.append(l[i-1] + l[i-2])
        # return l[-1]

        # variable based
        a = 0
        b = 1

        for i in range(N - 1):
            c = a
            a = b
            b = c + a
        return b