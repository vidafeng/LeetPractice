class Solution:
    def isValid(self, s: str) -> bool:
        # last type of bracket that is opened
        # must be the FIRST one to be closed --> LIFO
        # use stack to keep track of all brackets

        # create brackets pairs dictionary
        # intiate stack
        # loop through string
            # if current is in dictionary, add to stack
            # else
            # it must be a closing bracket
            # pop off top of stack
            # check if current == value
            # if not equal or if stack is empty, return false


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
