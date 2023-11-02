class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if current element i is NOT equal to previous element it means we have encountered a new unique element
        # update nums[j] with the value of the unique element at nums[i]
        # increment j by 1
        # this overwrites any duplicates in the array and only keep unique elements
        # return the number of unique elements in nums

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j



        