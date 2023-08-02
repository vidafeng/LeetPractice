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
        # n = len(nums)
        # maximumSum, currSumSubarray = float('-inf'), 0
        # for i in range(n):
        #     currSumSubarray += nums[i]
        #     maximumSum = max(maximumSum, currSumSubarray)
        #     currSumSubarray = max(currSumSubarray, 0)
        # return maximumSum

        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i...
            # then its value should be the larger one between nums[i]...
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
            # calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...