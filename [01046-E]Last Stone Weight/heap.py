class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # all stones have a positive weight
        for i in range(len(stones)):
            stones[i] *= -1
        
        # sort stone using min stack
        heapq.heapify(stones)
       
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
        return -heapq.heappop(stones) if len(stones) else 0

# Runtime: 32 ms, faster than 40.92% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
# method: heap