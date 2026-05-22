class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m + n
        temp = [num for num in nums1]
        print(temp)
        while i > 0 and m > 0 and n > 0:
            if temp[m-1] > nums2[n-1]:
                nums1[i-1] = nums1[m-1]
                m -= 1
            else:
                nums1[i-1] = nums2[n-1]
                n -= 1
            i -= 1
        while i > 0 and m == 0:
            nums1[i-1] = nums2[n-1]
            n -= 1
            i -= 1
        
        while i > 0 and n == 0:
            nums1[i-1] = nums1[m-1]
            m -= 1
            i -= 1
        

        