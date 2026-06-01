class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {ch:t.count(ch) for ch in set(t)}
        window = {}
        left = 0
        right = 0
        have = 0
        min_length = float('inf')
        result = ""
    

        while right < len(s):
            if s[right] in t_count:
                window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1
            right += 1
            
            while have == len(t_count):

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right]
                
                removed_char = s[left]
                
                if removed_char in t_count and window[removed_char] == t_count[removed_char]:
                    have -= 1 # this makes it invalid
                
                if removed_char in window:
                    window[removed_char] -= 1
                
                left += 1
        return result


  
        