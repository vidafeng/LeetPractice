class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict = {
            "(":")",
            "{":'}',
            "[": ']'

        }


        for char in s:
            if char in dict:
                stack.append(char)
            elif len(stack) == 0 or char != dict[stack.pop()]:
                return False


      


        
        return len(stack) == 0
