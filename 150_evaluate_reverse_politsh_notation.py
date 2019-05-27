class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                else:
                    z = x / y
                    if z > 0:
                        z = math.floor(z)
                    else:
                        z = math.ceil(z)
                    stack.append(z)
            else:
                stack.append(int(token))
        return stack[0]

# Runtime: 44 ms, faster than 87.53% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 13.3 MB, less than 62.82% of Python3 online submissions for Evaluate Reverse Polish Notation.