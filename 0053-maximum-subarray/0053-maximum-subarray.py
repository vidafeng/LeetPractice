class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep track of currentSum of subArray
        # whenever currentSum is greater than maxSum, update maxSum
        # if currentSum becomes negative, reset sum to 0 and start new subArray

        # initialize maxSum and currentSum
        # iterate through the nums array using for loop

        # currentSum = 0
        # maxSum = 0

        # for num in nums:
        #     currentSum += num

        #     if currentSum > maxSum:
        #         maxSum = currentSum
            
        #     if currentSum < 0:
        #         currentSum = 0
        
        # return maxSum
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum