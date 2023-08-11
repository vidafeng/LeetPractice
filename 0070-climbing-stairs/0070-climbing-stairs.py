class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci series
        # base cases are when we are on the 
            # 1st stair -- only one way to reach it
            # 2nd stair -- 2 ways to reach it
            # by summing up the number of ways to reach the n-1 and n-2 stairs
            # we can compute the total number of ways to climb the stairs



        prev = 1
        curr = 1

        for i in range(2, n+1):
            temp = curr 
            curr = prev + curr
            prev = temp
        return curr