class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_previous = 1
        right_previous = 1
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        for index, num in enumerate(nums):
            left_product[index] = left_previous
            left_previous = left_previous * num

        for index in range(len(nums))[::-1]:
            right_product[index] = right_previous
            right_previous = right_previous * nums[index]
        
        result = []
        for i in range(len(left_product)):
            result.append(left_product[i] * right_product[i])
        return result


        