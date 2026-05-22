class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for index, num in enumerate(nums):
            if num in result:
                if index - result[num] <= k:
                    return True
                else:
                    result[num] = index 
            else:
                result[num] = index
        return False 