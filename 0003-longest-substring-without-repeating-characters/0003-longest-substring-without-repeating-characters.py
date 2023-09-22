class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        # Iterate through string using two pointers
        # Use charSet to keep track of unique characters in current substring 
        # Iterate through string using the right pointer
        # If current character is not in charSet we have a unique char
        # Insert the current char into the set and update max length
        # Else if char is present in set, indicates repeating char
        # Move the left pointer forward
        # Remove charaters from set until repeating char is gone
        # Insert current character into set and continue iteration
        # Return maxLength
        n = len(s)
        maxLength = 0
        currentLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                print("if", charSet)
                maxLength = max(maxLength, right - left + 1)
                print("maxl", maxLength)
            else: 
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])


        return maxLength

        