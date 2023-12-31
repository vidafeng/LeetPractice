class Solution:
    def isPalindrome(self, s: str) -> bool:
# change all letters to lowercase
# remove spaces and punctuation

# two pointer strategy
# left pointer at index 0
# right pointer at end of string
# check characters at index l if they are either letters or nums
# if not, increment by 1 
# check characters at index r if they are either letters or nums 
# if not, decrement by 1 
# if current characters at index l and r are letters or nums, check against each other
# if not the same, return false
# if same, increment l by 1 and decrement r by 1

        l = 0
        r = len(s) - 1
        

        while l < r: 
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif  s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True
            
            
            
        
        
        

    
        
        