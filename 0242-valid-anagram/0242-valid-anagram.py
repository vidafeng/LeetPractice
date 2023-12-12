class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# hash map 
# if hash map is the same then return true

        hashS = {} 
        hashT = {}
        
        for char in s:
            if char not in hashS:
                hashS[char] = 1
            else: 
                hashS[char] += 1
        
        for char in t:
            if char not in hashT:
                hashT[char] = 1
            else: 
                hashT[char] += 1
                
        if hashS == hashT:
            return True
        
        return False
            
    
        
        