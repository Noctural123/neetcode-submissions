class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one



    # bruh, fibb but easy ass solution somehow idk, sohuld O(n) time and O(1) space or some shit