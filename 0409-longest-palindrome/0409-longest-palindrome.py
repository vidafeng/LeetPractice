class Solution:
    def longestPalindrome(self, s: str) -> int:
        # initialize two variables
        # oddcount to store the num of char with odd occurences
        # unordered hashmap to store count of each char in str
        # if count of current char is odd, increment oddCount
        # else decrement oddCount
        # if oddCount is greater than 1 return s.length() - oddCount + 1
            # max length of palindrome that can be formed using all but one char
        # if oddCount is not greater than 1, return s.length()
            # length of original str, since all char can be used to form palindrome 
        oddCount = 0
        dict = {}

        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1

            if dict[char] % 2 == 1:
                oddCount += 1
            else: 
                oddCount -= 1
            
        if oddCount > 1:
            print(oddCount)
            return len(s) - oddCount + 1
        else: 
            return len(s)

        