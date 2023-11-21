class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# HASH MAP METHOD
#         hash = {}
        
#         for num in nums:
#             if num in hash:
#                 return True
#             else:
#                 hash[num] = 1
        
#         return False

# HASH SET METHOD o(n)
# hash data structure to store encountered elements
# iterate thru the array
# if element is not in set, add
# otherwise, return True
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False



# BRUTE FORCE METHOD - time till exceed
# compare each element with every other element in the array for duplicates
# time complexity is o(n^2), not efficient for large arrays

        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
