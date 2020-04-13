class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:

            stones = sorted(stones)
            # print(stones)
            y = stones.pop()
            x = stones.pop()
            if x != y and y > x:
                stones.append(y-x)
        return stones[0] if len(stones) else 0

# Runtime: 32 ms, faster than 40.92% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
# method: sort 