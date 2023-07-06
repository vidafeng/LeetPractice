class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create hash map to keep track of # of letters in magazine
        # loop thru ranson note
        # if letter is in hash, decrement
        # if letter is not in hash, return false 
        # return true

        # dict = {}

        # for char in magazine:
        #     if char not in dict:
        #         dict[char] = 0
        #     dict[char] += 1
        
        # for char in ransomNote:
        #     if char not in dict or dict[char] == 0:
        #         return False
        #     else:
        #         dict[char] -= 1
            
        # return True

        # iterate over each char in ransomNote str
        # for each char, check if present in magazine string
        # if char is found, remove char from magazine str
        # remove method only on lists
        # if not found, immediately return False
        # return true if we have successfully removed each char from magazine str

        magazine = list(magazine)

        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True
