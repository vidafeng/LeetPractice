class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left and right pointer
        # keep track of seen chars, longest length 
        # loop through the string
            # need index!!!
            # if char is in seen
              # update left pointer to the index + 1 of same char (look up)

         # if char is NOT seen
             # calculate length and compare to prev longest length 
          # update seen to current index
            # return length 

        pointer = 0

        seen = {}
        longestLength = 0

        for i in range(len(s)):
            char = s[i]

            if char in seen and seen[char] >= pointer:
                pointer = seen[char] + 1
            else:
                longestLength = max(i-pointer + 1, longestLength)

            seen[char] = i

        return longestLength


