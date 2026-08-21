class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ""
        cur_num = 0
        stack = []
        for char in s:
            if char.isalpha():
                cur_str += char
            elif char.isnumeric():
                cur_num = (cur_num * 10) + int(char)
            elif char == "[":
                stack.append((cur_num, cur_str))
                cur_str = ""
                cur_num = 0
            elif char == "]":
                popped_item = stack.pop()
                cur_str = cur_str * popped_item[0]
                popped_str = popped_item[1]
                popped_str += cur_str
                cur_str = popped_str
        return cur_str



        