class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = left
        max_length = 0
        string_length = 0
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
            else:
                left += 1
                right = left
                window = set()
                continue
            string_length = right - left + 1
            max_length = max(max_length, string_length)
            right += 1
        return max_length
    

        