var removeDuplicates = function(nums) {
    let count =1;
    for (let i = 1; i < nums.length; i++){
        if (nums[i] != nums[count-1]){
            nums[count] = nums[i];
            count ++;
        }
    }

    return count;
}

const nums = [0,0,1,1,1,2,2,3,3,4];
console.log(removeDuplicates(nums));
console.log(nums);