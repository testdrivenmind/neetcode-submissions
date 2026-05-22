class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_nums =  sorted(set(nums))
        count = 0
        max_count = 0
        for i in range(1,len(new_nums)):
            j = i - 1
            if new_nums[i] == new_nums[j] + 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count + 1