class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scanning
        # initalize base variable as first word
        # iterate thru each letter of the base word
        # iterate through the list of strings starting from idx one
            # check each letter against the base word
            # if letters do not match return prefix slice

        if len(strs) == 0:
            return ""
        
        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if i ==len(word) or base[i] != word[i]:
                    return base[0:i]
        return base

