/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // dictionary method
    // loop through s and create a dictionary of all letter and occurences
    // loop through t and check if the letter is a key in the dictionary
        // if yes, decrease occurence
    // loop through dictionary, if any value does not equal 0 return false
        // all letter vals  should be 0 if strings are anagrams

    let dict = {};

    for (let char of s) {
        if (!(char in dict)) {
            dict[char] = 0;
        }
            dict[char] += 1;
    }

    for (let char of t) {
        if (dict[char] === undefined) {
            return false
        } else {
            dict[char] -= 1;
        }
    }

    for (let key in dict) {
        if (dict[key] !== 0) {
            return false;
        }
    }
    return true;
    
};