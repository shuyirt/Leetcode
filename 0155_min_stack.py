class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        if self.list:
            self.min = min(self.list)
        return

    def pop(self):
        """
        :rtype: None
        """
        remove = self.list.pop()
        if self.list:
            self.min = min(self.list)
        return

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()