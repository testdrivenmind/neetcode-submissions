class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if len(nums) == 0:
            return -1
        elif target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        elif target > nums[mid]:
            res = self.search(nums[mid+1:], target)
            if res != -1:
                return (mid + 1) + res
            return -1
        else:
            return -1
        