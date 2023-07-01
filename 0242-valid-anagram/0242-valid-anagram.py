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
            # get method to increment the count of char if it alrdy exists, otherwise set the count to 1
        
        for char in t: 
            if char not in hash or hash[char] == 0:
                return False
            else:
                hash[char] -= 1

        return True


# time complexity: o(n) where n is the legnth of the longer string since we need to iterate over each character of both strings once

# space is o(n) bc we use hash map to store frequency of char in the first string


