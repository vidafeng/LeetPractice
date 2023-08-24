class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return -1 if haystack is smaller than needle
        if len(haystack) < len(needle):
            return -1

        # return 0 if haystack and needle is length 1
        if len(haystack) == len(needle) == 1 and haystack[0]==needle[0] :
            return 0

        for i in range(len(haystack)):                
            start = i
            j = 0

            while(haystack[i] == needle[j]):
                
                # return start index if end of needle reached because end also matched 
                if j == len(needle)-1:
                    return start

                i += 1
                j += 1

            #return  -1 if end of haystack reached and substr didnt match 
                if i == len(haystack):
                    return -1
            
        return -1