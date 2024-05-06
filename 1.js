var twoSum = function(nums, target){
    let left = 0;
    let right = nums.length - 1;
    while (left < right){
        if (nums[left] + nums[right] < target){
            left += 1;
            console.log("smaller");
        } else if (nums[left] + nums[right] > target){
            right -= 1;
            console.log("larger");
        } else {
            // return [left, right];
            console.log("perfect");
            return([left, right]);
        }
    }
};


nums = [2,7,11,15];
target = 9;
console.log(twoSum(nums, target));