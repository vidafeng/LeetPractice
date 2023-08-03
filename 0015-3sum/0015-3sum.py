class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer BRUTE FORCE
        # sort the array
        # loop through each ele of array, up to len - 2
            # this is bc we need at least 3 ele to form triplet
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                secondNum  = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    triplets.add((firstNum , secondNum ,thirdNum))
                    j += 1
                    k -= 1
        return triplets