class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash = {}

        # for num in nums:
        #     if num in hash:
        #         hash[num] += 1
        #     else:
        #         hash[num] = 1

        # for num in hash:
        #     if hash[num] == 1:
        #         return num

# create a set for nums array
    # set removes all duplicate values
# loop thru set
# if nums.count for current i is equal to 1
# return i
        for i in set(nums):
            if nums.count(i) == 1:
                return i
