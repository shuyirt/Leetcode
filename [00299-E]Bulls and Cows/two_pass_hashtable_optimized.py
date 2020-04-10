class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = sum(secret[i] == guess[i] for i in range(len(secret)))
        cs = collections.Counter(secret)
        cg = collections.Counter(guess)
        cows = 0
        for d in cs&cg:
            cows += min(cs[d], cg[d])
        cows -= bull
        return str(bull) + 'A' + str(cows) + 'B'

# Runtime: 28 ms, faster than 98.80% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.6 MB, less than 25.00% of Python3 online submissions for Bulls and Cows.
# method: two pass + hashtable
# first pass, filter out Bulls
# second pass, calculate cows