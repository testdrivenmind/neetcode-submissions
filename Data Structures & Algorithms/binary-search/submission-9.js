class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        function helper(left, right) {
            let mid = Math.floor((left + right) / 2)
            if(left > right) return -1
            
            if (target === nums[mid]) return mid;
            else if (target < nums[mid]) return helper(left, mid - 1)
            else return helper(mid + 1, right)
        }
        return helper(0, nums.length - 1)
    }
}
