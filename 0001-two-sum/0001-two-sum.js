/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // loop through nums array
    // create a hash map to keep track of previous visited nums = index

    // initialize complment = target - currentnum 
    // check if complement is in previous num
    // if yes, return value for corresponding key, and current index


    let previousNum = {};

    for (let i = 0; i < nums.length; i++) {
        let currentNum = nums[i];

        let complement = target - currentNum;

        if (complement in previousNum) {
            return [previousNum[complement], i];
        }

        previousNum[currentNum] = i; 
    }
};