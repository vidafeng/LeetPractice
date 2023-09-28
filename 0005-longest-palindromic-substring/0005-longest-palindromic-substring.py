class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans
        # def expand(l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return s[l+1:r]

        # result = ""
        # for i in range(len(s)):
        #     sub1 = expand(i, i)
        #     if len(sub1) > len(result):
        #         result = sub1
        #     sub2 = expand(i, i+1)
        #     if len(sub2) > len(result):
        #         result = sub2
        # return result