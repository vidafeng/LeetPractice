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

        # create stack data structure
        stack = []
        # create dictionary for opening closing pairs 
        dict = {
            "(":")",
            "{":'}',
            "[": ']'

        }

        # traverse each char in input string 
        for char in s:
            # if char is key in dictionary, append to stack 
            if char in dict:
                stack.append(char)
            # if char is closing parens, check if that same type opening parens is at the top of the stack
            # if not, return false 
            elif len(stack) == 0 or char != dict[stack.pop()]:
                return False
        # check if stack is empty or not
        # if stack is empty it means every opened parens is closed
        # otherwise, we return false
        return len(stack) == 0
