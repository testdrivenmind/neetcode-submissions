class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        expected_times = len(nums) // 2
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        for k, v in count_map.items():
            if v >= expected_times:
                return k
        

        