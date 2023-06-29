/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // two pointers method
    // convert all uppercase to lowercase letters
    // remove all nonalphanumeric characters

    // left pointer at index 0
    // right pointer at s.length-1

    // while left < right pointer
    // if s[left] is the same as s[right] 
    // increment left
    // decrement right
    // else return false 

    // return true
    
    let str = s.replace(/[^a-z0-9]/gi, '').toLowerCase()
    let left = 0;
    let right = str.length-1; 

    while (left <= right) {
        if (str[left] === str[right]) {
            left += 1;
            right -= 1;
        } else {
            return false;
        }
    }
    return true;
};