class Solution:
    def isValid(self, s: str) -> bool:
        result_stack = []
        len_of_s = len(s)
        
        if len_of_s == 0:
            return False
        
        if len_of_s % 2 != 0:
            return False
        
        for ch in s:
            if ch == "{" or ch == "[" or ch == "(":
                result_stack.append(ch)
            if ch == "}" or ch == "]" or ch == ")":
                if result_stack:
                    res = result_stack.pop()
                else:
                    return False
            if (ch == "}" and res != "{") or (ch == "]" and res != "[") or (ch == ")" and res != "("):
                return False
        
        return len(result_stack) == 0


             