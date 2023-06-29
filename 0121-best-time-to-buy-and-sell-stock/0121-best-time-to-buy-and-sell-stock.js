/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // two pointer strategy
    // loop thru prices until right pointer is less than/equal to prices length

    // if leftPrice is less than rightPrice, calculate currentProfit by subtacting
    // check if currentProfit is greater than the maxProfit, 
        // if yes, reassign maxProfit
        // increment right pointer
    // else move our left pointer to be the minimum (rightPrice, j)
        // increment right pointer
    // we always want leftPrice to be LESS in order to gain profit from selling

    // return maxProfit


    let maxProfit = 0; 
    let i = 0;
    let j = i + 1;

    while (j <= prices.length) {

        if (prices[i] < prices[j]) {
            let currentProfit = prices[j] - prices[i];
            maxProfit = Math.max(maxProfit, currentProfit)
        } else {
            i = j;
        }
        j += 1;
    }
    
    return maxProfit;
    
};