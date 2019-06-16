class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        count = 0
        sign = "+"
        for i , v in enumerate(s):
            if v.isdigit():
                count = count *10 + int(v)
            if v in '-+*/' or i == len(s)-1:
                if sign == '-':
                    stack.append(-count)
                elif sign == '+':
                    stack.append(count)
                elif sign == '*':
                    stack.append(stack.pop()*count)
                else:
                    z = stack.pop()/count
                    z = math.floor(z) if z > 0 else math.ceil(z)
                    stack.append(z) 
                sign = v
                count = 0
        return sum(stack)

# Runtime: 88 ms 92.43%
# Memory Usage: 14.8 MB 75%