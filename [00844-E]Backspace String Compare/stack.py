class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.editorProcessor(S) == self.editorProcessor(T)
    def editorProcessor(self, string: str) -> str:
        res = collections.deque()
        l = 0
        for i in string:
            if i == "#":
                if  l > 0: 
                    res.pop()
                    l -= 1
            else:
                res.append(i)
                l += 1
        return ''.join(list(res))


# Runtime O(M+N): 16 ms, faster than 99.68% of Python3 online submissions for Backspace String Compare.
# Memory Usage O(M+N): 13.6 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.
# method: stack
# build two string using stack, and compare the result