class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = sorted(set(nums))
        nums[:] = k
        print(k)
        return len(nums)