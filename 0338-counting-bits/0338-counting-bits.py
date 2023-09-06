class Solution:
    def countBits(self, n: int) -> List[int]:
        # use the number of 1's in i >>
        # >> right shift operator

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

        