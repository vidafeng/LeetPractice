/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // create a stack
    // create an object look up
    // loop through s
    // if char is in brackets
    // add corresponding value to stack
    // if next char matches top of stack, pop

    let stack = [];
    const brackets = { "(":")", "[":"]", "{":"}" };

    for (char of s) {
        if (char in brackets) {
            stack.push(brackets[char])
        } else {
            if (stack.length > 0 && char === stack[stack.length-1]) {
                stack.pop();
            } else {
                return false
            }
        }
    }
    return stack.length === 0;
    
};