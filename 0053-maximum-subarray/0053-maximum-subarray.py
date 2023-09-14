class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Iterate through the array and keep track of the current sum
        # When current sum > max sum, update max sum
        # When current sum is negative, reset to 0

        currentSum = 0
        maxSum = float('-inf')

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0

        return maxSum


        