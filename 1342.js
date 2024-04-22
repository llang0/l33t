// 1342. Number of Steps to Reduce a Number to Zero
// Given an integer num, return the number of steps to reduce it to zero.

// In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

/**
 * @param {number} num
 * @return {number}
 */

 // this feels recursive


 function reduce(num, steps) {
    if (num === 0){
        return steps;
    } else {
        if (num%2 === 0){
            num = num/2
        } else {
            num -= 1;
        }
        steps++;
        return reduce(num, steps);
    }
};

var numberOfSteps = function(num) {
    return reduce(num, 0);
};

