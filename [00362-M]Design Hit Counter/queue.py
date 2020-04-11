class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._shot_queue = collections.deque()
        self._range = 300
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        while self._shot_queue:
            if timestamp - self._range > self._shot_queue[0] :
                self._shot_queue.popleft()
            else:
                break
        self._shot_queue.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self._shot_queue:
            if timestamp - self._range >= self._shot_queue[0] :
                self._shot_queue.popleft()
            else:
                break
        return len(self._shot_queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# Runtime: 16 ms, faster than 82.95% of Python online submissions for Design Hit Counter.
# Memory Usage: 12.9 MB, less than 25.00% of Python online submissions for Design Hit Counter.
# method: queue