class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    
    # def charCount(self, str):
    #     count = {}

    #     for char in str:
    #         if char not in count:
    #             count[char] = 0
    #     count[char] += 1
    
    #     return count
