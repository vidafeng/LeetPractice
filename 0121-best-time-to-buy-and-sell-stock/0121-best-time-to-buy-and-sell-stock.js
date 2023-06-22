/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // two pointers buy, sell at first pos and second pos of array
    // initialize maxProfit
    // we always want left pointer to be less than right pointer (for profit)
    // return the maximum profit you can achieve

    let i = 0;
    let j = 1; 

    let maxProfit = 0;

    while (i < prices.length) {
        if (prices[i] < prices[j]) {
            let currentProfit = prices[j] - prices[i]
            if (currentProfit > maxProfit) {
                maxProfit = currentProfit;
            }
        } else { 
            i = j;
        }
        j += 1;
    }
    return maxProfit; 

};