class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = ""
        for word in words:
            word = word[::-1]
            result += word + " "
            print(word)
        return result[:-1]