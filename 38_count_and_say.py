class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        if n == 1:
            return ans

        for i in range(1, n):
            c = ans[0]
            count = 0
            temp = ''
            for letter in ans:
                if c == letter:
                    count += 1
                else:
                    temp += "{}{}".format(count, c)
                    count = 1
                    c = letter
            temp += "{}{}".format(count, c)
            ans = temp
        return ans