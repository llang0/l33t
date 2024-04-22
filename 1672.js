// 1672. Richest Customer Wealth

// You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

// A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

// Example 1:

// Input: accounts = [[1,2,3],[3,2,1]]
// Output: 6
// Explanation:
// 1st customer has wealth = 1 + 2 + 3 = 6
// 2nd customer has wealth = 3 + 2 + 1 = 6
// Both customers are considered the richest with a wealth of 6 each, so return 6.

/**
 * @param {number[][]} accounts
 * @return {number}
 */
 // i is the customer 
 // j is the bank
 // accounts[i][j] is the amount in that account

 var maximumWealth = function(accounts) {
    richest = 0;  // holds the wealth of the richest customer

    // iterate one time through all items in array
    for (i = 0; i < accounts.length; i++){
        // for every customer
        sum = 0; // create an int to hold the total wealth

        // iterate through their accounts
        for (j = 0; j < accounts[i].length; j++){
            // sum their accounts
            sum += accounts[i][j]
        }

        // if they are richer than the previous richest customer
        if (sum > richest){
            // they are the new richest customer
            richest = sum;
        }
    }
    return richest;
};