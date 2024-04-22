// 412. Fizz Buzz

// Given an integer n, return a string array answer (1-indexed) where:

// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.

// Example 1:

// Input: n = 3
// Output: ["1","2","Fizz"]

var fizzBuzz = function(n){
    let answer = [];
    
    // if an answer is divisble by both 3 and 5 it must also be divisble by 15
    for (i = 1; i <= n; i++){
        answer.push(
            (i % 15 === 0) ? "FizzBuzz" :
            (i % 3 === 0 ) ? "Fizz" :
            (i % 5 === 0) ? "Buzz" :
            i.toString()
        );
    }

    return answer;
}