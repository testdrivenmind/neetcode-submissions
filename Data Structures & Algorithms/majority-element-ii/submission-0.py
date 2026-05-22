class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        print(count_map)
        return [key for key,val in count_map.items() if val > limit]
        