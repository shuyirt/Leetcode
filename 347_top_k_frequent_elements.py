class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums).most_common(k)
        return [a[0] for a in count]

# Runtime: 44 ms, faster than 93.71% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 15.9 MB, less than 50.79% of Python3 online submissions for Top K Frequent Elements.

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 