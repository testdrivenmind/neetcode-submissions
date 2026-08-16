class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        for char in s:
            if char.isalpha():
                current_str += char
            elif char.isnumeric():
                current_num = (current_num * 10) + int(char)
            elif char == "[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == "]":
                popped_item = stack.pop()
                current_str = popped_item[1] * current_str
                popped_str = popped_item[0]
                popped_str += current_str
                current_str = popped_str
              
        return current_str