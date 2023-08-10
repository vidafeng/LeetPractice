class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert all char in s to lowercase

        res = ''
        s = s.lower()

        for char in s:
            if char.isalnum() or char.isnumeric():
                res += char
        print(res)
        
        return res == res[::-1]
         
        