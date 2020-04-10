class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.hashtable:
            self.hashtable[message] = timestamp 
            return True
        elif timestamp - self.hashtable[message] >= 10:
            self.hashtable[message] = timestamp 
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# Time Complexity: O(1). The lookup and update of the hashtable takes a constant time. 
# Space Complexity: O(M) where M is the size of all incoming messages. Over the time, the hashtable would have an entry for each unique message that has appeared. 
# Runtime: 152 ms, faster than 58.44% of Python3 online submissions for Logger Rate Limiter.
# Memory Usage: 19.9 MB, less than 20.00% of Python3 online submissions for Logger Rate Limiter.
# method: hashtable