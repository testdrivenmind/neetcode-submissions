class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        reference = {}
        
        for first_found_index, value in enumerate(nums):
            looking_for_num = target - value
            reference[looking_for_num] = first_found_index
        
        for index, value in enumerate(nums):
            if value in reference and index != reference[value]:
                if reference[value] < index:
                    return [reference[value], index]
                else:
                    return [index, reference[value]]

        