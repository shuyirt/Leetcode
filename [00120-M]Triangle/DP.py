class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        top = [triangle[0][0]]
        bottom = []
        
        for l in range(1, len(triangle)):
            for i in range(len(triangle[l])):
                top_value = 0
                if i == 0:
                    top_value = top[i]
                elif i + 1 > len(top):
                    top_value = top[i-1]
                else:
                    top_value = min(top[i-1], top[i])
                bottom.append(top_value + triangle[l][i])
            top = bottom
            bottom = []
        return min(top)

# Runtime O(n^2): 60 ms, faster than 66.78% of Python3 online submissions for Triangle.
# Memory Usage O(n): 14.2 MB, less than 20.00% of Python3 online submissions for Triangle.
# method: DP, top down
#  using 2 array to store the value