class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for l in s:
            if l == ']':
                cur = ''
                while stack:
                    r = stack.pop()

                    if r == '[':
                        num = ''
                        while stack and stack[-1].isdigit():
                            num = stack.pop() + num
                        stack.append(int(num) * cur)
                        break
                    else:
                        cur = r + cur

            else:
                stack.append(l)
        return "".join(stack)

# Runtime: 36 ms, faster than 86.34% of Python3 online submissions for Decode String.
# Memory Usage: 13.3 MB, less than 8.72% of Python3 online submissions for Decode String.