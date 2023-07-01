class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        hash = {}

        for char in s:
            hash[char] = hash.get(char, 0) + 1
        
        for char in t: 
            if char not in hash or hash[char] == 0:
                return False
            else:
                hash[char] -= 1
                
        return True


