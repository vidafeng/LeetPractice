class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create hash map to keep track of # of letters in magazine
        # loop thru ranson note
        # if letter is in hash, decrement
        # if letter is not in hash, return false 
        # return true

        dict = {}

        for char in magazine:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        
        for char in ransomNote:
            if char not in dict or dict[char] == 0:
                return False
            else:
                dict[char] -= 1
            
        return True

