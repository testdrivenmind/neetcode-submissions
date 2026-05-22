class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for index, num in enumerate(nums):
            if num in result and index - result[num] <= k:
               return True
            result[num] = index 
        return False 