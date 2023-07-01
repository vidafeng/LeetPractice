/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // dictionary method
    // loop through s and create a dictionary
    // see if the letters of t is in the dictionary

    let dict = {};

    for (let char of s) {
        if (!(char in dict)) {
            dict[char] = 0;
        }
            dict[char] += 1;
    }

    for (let char of t) {
        if (char in dict && dict[char] > 0) {
            dict[char] -= 1;
        } else {
            return false;
        }
    }

    for (let key in dict) {
        if (dict[key] !== 0) {
            return false;
        }
    }
    return true;
    
};