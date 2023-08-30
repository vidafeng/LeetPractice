class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1


        # # iterate through the list
        # # move all non zero elements to the begininf of the list
        # index = 0

        # # Place non-zero elements at the start of the list
        # for num in nums:
        #     if num != 0:
        #         nums[index] = num
        #         index += 1

        # # Fill the remaining positions with zeroes
        # while index < len(nums):
        #     nums[index] = 0
        #     index += 1