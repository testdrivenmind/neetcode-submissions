class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        write = 0
        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                nums.append(val)
                write += 1
            read = read + 1    
        return len(nums[:write])
