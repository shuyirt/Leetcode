class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.capacity = size
        self.size = 0
        self.queue = collections.deque([], size)
        self.total = 0

    def next(self, val: int) -> float:
        if self.size == self.capacity:
            v = self.queue.popleft()
            self.total -= v
            self.size -= 1
        self.queue.append(val)
        self.total += val
        self.size += 1

        return self.total / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Runtime: 56 ms, faster than 98.04% of Python3 online submissions for Moving Average from Data Stream.
# Memory Usage: 16.3 MB, less than 68.08% of Python3 online submissions for Moving Average from Data Stream.