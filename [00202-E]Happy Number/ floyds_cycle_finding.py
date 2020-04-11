class Solution:
    def isHappy(self, n: int) -> bool:
        slow_runner = n
        fast_runner = self.calculateHappy(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.calculateHappy(slow_runner)
            fast_runner = self.calculateHappy(self.calculateHappy(fast_runner))
        return fast_runner == 1 

    
    def calculateHappy(self, n:int) -> int:
        return sum([int(i)**2 for i in str(n) ])

# Runtime: 40 ms, faster than 18.47% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Happy Number.
# method: Floyd's Cycle-Finding Algorithm

# This algorithm is based on 2 runners running around a circular race track, a fast runner and a slow runner. In reference to a famous fable, many people call the slow runner the "tortoise" and the fast runner the "hare".

# Regardless of where the tortoise and hare start in the cycle, they are guaranteed to eventually meet. This is because the hare moves one node closer to the tortoise (in their direction of movement) each step.

# Instead of keeping track of just one value in the chain, we keep track of 2, called the slow runner and the fast runner. At each step of the algorithm, the slow runner goes forward by 1 number in the chain, and the fast runner goes forward by 2 numbers (nested calls to the getNext(n) function).

# If n is a happy number, i.e. there is no cycle, then the fast runner will eventually get to 1 before the slow runner.

# If n is not a happy number, then eventually the fast runner and the slow runner will be on the same number.