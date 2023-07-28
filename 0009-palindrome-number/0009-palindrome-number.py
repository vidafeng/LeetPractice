class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is neg, return false

        if x < 0:
            return False
            
        x = str(x)
        i = 0
        j = len(x)-1

        while i < j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else: 
                return False
        return True


