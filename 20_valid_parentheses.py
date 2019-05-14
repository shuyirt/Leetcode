class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # using stack to solve this question, last in last out

        stack = []

        pair = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        '''
            case1: '['
            case2: ']'
            case3: '[]'
            case4: '[(])'
        '''
        for x in s:
            if not x in pair:
                stack.append(x)
            elif len(stack) == 0:
                return False
            elif pair[x] == stack[-1]:
                stack.pop()
            else:
                return False

        return not len(stack)

# Runtime: 20 ms, faster than 93.23% of Python online submissions for Valid Parentheses.
# Memory Usage: 11.9 MB, less than 5.20% of Python online submissions for Valid Parentheses.