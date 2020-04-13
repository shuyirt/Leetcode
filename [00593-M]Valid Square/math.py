class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        length = [self.distance(p1,p2), self.distance(p1,p3), self.distance(p1,p4), self.distance(p2,p3), self.distance(p2,p4), self.distance(p3,p4)]
        length.sort()
        
        if length[0] == 0:
            return False
        
        for i in range(3):
            if length[i] != length[i+1]:
                return False
        
        return length[-1] == length[-2]
    
    def distance(self, a: List[int], b: List[int])-> int:
        x = a[0] - b[0]
        y = a[1] - b[1]
        return x**2 + y**2

# Runtime: 32 ms, faster than 66.06% of Python3 online submissions for Valid Square.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Valid Square.
# method: math