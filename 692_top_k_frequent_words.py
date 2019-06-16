class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_table = collections.Counter(words)
        keys = list(hash_table.keys())
        keys.sort(key=lambda x:(-hash_table[x], x))
        
        return keys[:k]

# Runtime: 44 ms, faster than 85.16% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 13 MB, less than 92.10% of Python3 online submissions for Top K Frequent Words.