class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = left
        max_length = 0
        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
    

        