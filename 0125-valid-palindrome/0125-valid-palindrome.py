class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert all char in s to lowercase
        # initialize empty result string
        # iterate over given string by converting to lowercase
        # check if corresponding value is character or num
            # if it is, add to result string
        # check if result string is palidrone by slicing from end

        res = ''
        s = s.lower()

        for char in s:
            if char.isalnum():
                res += char
        print(res)
        
        return res == res[::-1]
         
        