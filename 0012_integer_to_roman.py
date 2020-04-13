class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        tens = 1
        while num > 0:
            r = num % 10
            num = num // 10

            if r in mapping:
                res = mapping[r * tens] + res
            elif r // 5 == 0:
                res = mapping[tens] * r + res
            else:
                res = mapping[5 * tens] + mapping[tens] * (r - 5) + res
            tens *= 10
        return res

# Runtime: 52 ms, faster than 95.42% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.1 MB, less than 91.02% of Python3 online submissions for Integer to Roman.


# a clever way posted by moevery
class Solution1(object):
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result