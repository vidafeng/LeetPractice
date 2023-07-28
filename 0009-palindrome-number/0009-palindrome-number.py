class Solution:
    def isPalindrome(self, x: int) -> bool:
# CHANGING NUM TO STR + USING TWO POINTERS
        # # if x is neg, return false

        # if x < 0:
        #     return False

        # x = str(x)
        # i = 0
        # j = len(x)-1

        # while i < j:
        #     if x[i] == x[j]:
        #         i += 1
        #         j -= 1
        #     else: 
        #         return False
        # return True

# REVERSING ENTIRE NUMBER
    # two variables:
        # reversed = stores the reversed value of number x, initializes to 0
        # temp = temp placeholder to manipulate input num

    # while temp is not 0
        # grab last digit of temp by using %10
        # store it as digit variable
        # to reverse the num, multiply reversed * 10 + digit
        # divide temp by 10 to remove last digit and move onto the next iteration


        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
            # print('digit', digit)
            # print('reversednum', reversed_num)
            # print('temp,', temp)

        return reversed_num == x


