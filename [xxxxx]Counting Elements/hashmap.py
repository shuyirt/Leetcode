class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashtable = collections.Counter(arr)
        counter = 0
        for item in arr:
            if item+1 in hashtable:
                hashtable[item+1] -= 1
                counter += 1
        return counter

# time: O(n)
# space: O(1)
# Runtime: 36 ms
# Memory Usage: 14.1 MB
# method: hash map, it is more scalable solution incase the time of mapping increases