class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Runtime: 124 ms, faster than 68.06% of Python3 online submissions for LRU Cache.
# Memory Usage: 21.7 MB, less than 70.87% of Python3 online submissions for LRU Cache.