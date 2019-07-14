# heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# Runtime: 36 ms, faster than 96.65% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 13.7 MB, less than 50.16% of Python3 online submissions for Kth Largest Element in an Array.