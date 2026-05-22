from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        right = left
        max_size = 0

        while right < len(s):
            char_count[s[right]] += 1
            if right - left + 1 - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
            right += 1
        return max_size


            


        