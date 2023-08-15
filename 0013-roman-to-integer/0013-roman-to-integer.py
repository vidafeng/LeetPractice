class Solution:
    def romanToInt(self, s: str) -> int:
        # when a smaller value appears before a larger value --> sub
        # when smaller value appears after larger value --> add

        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and hash[s[i]] < hash[s[i+1]]:
                res -= hash[s[i]]
            else: 
                res += hash[s[i]]

        return res



