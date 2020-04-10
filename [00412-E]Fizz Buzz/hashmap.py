class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        # store all mapping s 
        mapping = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n+1):
            s = ''
            for key in mapping.keys():
                if not i % key:
                    s += mapping[key]
            
            if not s:
                s = str(i)
            result.append(s)
        return result

# time: O(n)
# space: O(1)
# method: hash map, it is more scalable solution incase the time of mapping increases