 class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0 
        for i in nums:
            a ^= i
        return a

# space: O(1) 15.2mb - 8.20%
# time:  O(n) 80ms - 95.72% O(n)
# method: bit manipulation

# or use hashmap:
# empty hash map
# try pop, it fail do append
# return the one last in hash map