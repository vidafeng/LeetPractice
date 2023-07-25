class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
# BRUTE FORCE -- time limit exceed
# comparing every num with the other nums in the arr
# o (n^2) time bc we are visiting every element in the arr twice

#         n = len(nums)
    
#         for i in range(0, n-1):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

# SORT
# sort the num arr and then loop
# if i is equal to i-1, then we have a duplicate
        
        nums.sort()
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
            
        return False
            
    
        