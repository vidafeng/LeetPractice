class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
# two pointers to iterate over both strings
# pointers i and j
# append the letter pointed by the pointer i
# increment i pointer
# append the letter pointed by the pointer j
# increment j pointer
# result is a list so must join at the end

        i = 0
        j = 0
        result = []
    
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1
        
        return "".join(result)
        