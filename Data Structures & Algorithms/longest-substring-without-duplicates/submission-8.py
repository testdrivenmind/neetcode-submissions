class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        left = 0
        right = left
        max_length = 0
        while right < len(s):
            if s[right] in index_map:
                left = max(left, index_map[s[right]] + 1)
            index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
    

        