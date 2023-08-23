class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers method
        # compare each element to the previous element to check for dup
        # if i is not equal to i-1
            # we have new unique element
        # update j to element at i
        # increment j by 1 for next position
        
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j