class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string_contents = {}
        for element in s:
            if element in string_contents:
                string_contents[element] += 1
            else:
                string_contents[element] = 1
        for t_char in t:
            if t_char not in string_contents:
                return False
            string_contents[t_char] -= 1
        
        return all(value == 0 for value in string_contents.values())
