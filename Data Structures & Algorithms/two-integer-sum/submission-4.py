class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for index, num in enumerate(nums):
            missing_num = target - num
            if missing_num in sum_map:
                return [sum_map[missing_num], index]
            else:
                sum_map[num] = index
 

        