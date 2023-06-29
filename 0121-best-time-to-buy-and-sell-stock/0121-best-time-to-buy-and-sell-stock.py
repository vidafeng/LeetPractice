class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0;
        right = 1;
        maxProfit = 0;

        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left]
                if currentProfit > maxProfit: 
                    maxProfit = currentProfit
            else: 
                left = right
            
            right += 1
    
        return maxProfit

