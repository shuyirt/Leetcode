class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1] :
            self.minstack.append(x)


    def pop(self):
        """
        :rtype: None
        """

        temp = self.stack.pop()
        
        if temp == self.minstack[-1]:
            self.minstack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Runtime: 52 ms, faster than 85.03% of Python online submissions for Min Stack.
# Memory Usage: 16.7 MB, less than 6.67% of Python online submissions for Min Stack.
# method: two stack, all o(1) time