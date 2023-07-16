class Solution:
    def majorityElement(self, nums: List[int]) -> int:
# if element occurs more than n/2 times in the array
# it will always occupy the middle position when array is sorted
# sort the array and return the element at index n/2 


        nums.sort()
        n = len(nums)
        # return nums[int(n/2)]
        # floor division 
        return nums[n//2]

