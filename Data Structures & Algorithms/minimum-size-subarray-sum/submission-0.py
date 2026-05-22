import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        left = 0
        right = 0
        min_length = math.inf
        
        while right < len(nums):
            sum += nums[right]
            if sum >= target:
                min_length = min(min_length, right - left + 1)
                
            while sum - nums[left] >= target and left < len(nums):
                    min_length = min(min_length, right - left)
                    sum -= nums[left]
                    left += 1
            right += 1 
        
        if min_length == math.inf:
            return 0
        return min_length



        