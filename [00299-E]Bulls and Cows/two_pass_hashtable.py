class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess_dict = collections.Counter(guess)
        secret_dict = collections.Counter(secret)
        bull = 0
        cow = 0
        for i in range(len(guess)):
            item = guess[i]
            if secret[i] == item:
                bull += 1
                guess_dict[item] -= 1
                secret_dict[item] -= 1
        for key in guess_dict:
            cow += min(guess_dict[key], secret_dict[key])
        return "{}A{}B".format(bull, cow)

# Runtime O(n): 36 ms, faster than 82.21% of Python3 online submissions for Bulls and Cows.
# Memory Usage O(n): 13.8 MB, less than 25.00% of Python3 online submissions for Bulls and Cows.
# method: two pass + hashtable
# first pass, filter out Bulls
# second pass, calculate cows