class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iterate through the list
        # move all non zero elements to the begininf of the list
        index = 0

        # Place non-zero elements at the start of the list
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        # Fill the remaining positions with zeroes
        while index < len(nums):
            nums[index] = 0
            index += 1