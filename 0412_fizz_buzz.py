class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1,n+1):
            #             divisible_by_3 = (num % 3 == 0)
            #             divisible_by_5 = (num % 5 == 0)
            # if divisible_by_3 and divisible_by_5:
            #     # Divides by both 3 and 5, add FizzBuzz
            #     ans.append("FizzBuzz")
            # elif divisible_by_3:
            #     # Divides by 3, add Fizz
            #     ans.append("Fizz")
            # elif divisible_by_5:
            #     # Divides by 5, add Buzz
            #     ans.append("Buzz")

            if i % 15 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l