class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.minimum = 0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        if len(self.minstack) == 0 or x < self.minimum:
            self.minimum = x            
        self.minstack.append(x)
        
    def pop(self):
        """
        :rtype: None
        """

        temp = self.minstack.pop()
        if temp == self.minimum and len(self.minstack) > 0:
            self.minimum = min(self.minstack)
    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

Runtime: 52 ms, faster than 85.03% of Python online submissions for Min Stack.
Memory Usage: 16.8 MB, less than 6.67% of Python online submissions for Min Stack.
methods: stack to execute pop,push, top. use a val to hold a variable
