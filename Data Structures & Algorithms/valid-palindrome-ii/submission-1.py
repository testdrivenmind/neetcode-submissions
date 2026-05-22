class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def valid(s: str) -> bool:
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if valid(s[left+1:right+1]) or valid(s[left:right]):
                    return True
                return False
            left += 1
            right -= 1
        return True

        