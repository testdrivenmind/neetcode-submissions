class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        duplicate_map = {}
        
        for num in nums:
            if num in duplicate_map:
                duplicate_map[num] += 1
            else:
                duplicate_map[num] = 1
        print(duplicate_map)
    
        count = 0
        for index, num in enumerate(nums):
            if duplicate_map[num] > 1:
                nums[index] = 1000
                duplicate_map[num] -= 1
                count += 1
        
        unique = len(nums) - count
        nums.sort()
        nums = nums[:unique]
        print(nums)
        return len(nums)