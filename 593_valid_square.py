class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
            x = a[0]-b[0]
            y = a[1]-b[1]
            return abs(x*x+y*y)
        r = [dist(p1,p2), dist(p1,p4), dist(p3,p2), dist(p3,p4), dist(p1,p3), dist(p2,p4)]
        r.sort()
        if r[0]*r[1] == 0:
            return False
        for i in range(len(r)-3):
            if r[i] != r[i+1]:
                return False
        
        return r[-1] == r[-2]
    

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Valid Square.
# Memory Usage: 13 MB, less than 93.23% of Python3 online submissions for Valid Square.