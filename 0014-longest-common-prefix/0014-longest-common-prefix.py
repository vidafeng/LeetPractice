class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scanning
        # scan the first character of every word
        # then scan the second character
        # until a mismatch is found
        # return a slice of the string with the longest common prefix

        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base


        