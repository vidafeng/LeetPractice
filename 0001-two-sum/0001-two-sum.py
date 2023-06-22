class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop thru nums list
        # keep track of index
        # subtract target - current num
        # if the complement is in the list
        # find index of complement
        # make sure complementDiff does not equal current num index
        # if equal, continue the loop
        # else return -- we've found two sums! 

        a = 0

        for i in range(len(nums)):
            complement = target - nums[i];

            if complement in nums:
                a = nums.index(complement)
                if a == i:
                    continue
                break
        return i, a 
            