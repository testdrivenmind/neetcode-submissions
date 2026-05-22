class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_prefix_sum = 0
        prefix_sum = 0
        result_map = {0:1}
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in result_map:
                count_prefix_sum += result_map[prefix_sum - k]
            
            if prefix_sum in result_map:
                result_map[prefix_sum] += 1
            else:
                result_map[prefix_sum] = 1

        return count_prefix_sum


            
        
        