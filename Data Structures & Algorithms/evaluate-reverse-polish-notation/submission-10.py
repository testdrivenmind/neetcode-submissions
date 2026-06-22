class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        operands = ["*", "+", "-", "/"]
     
        for token in tokens:
            if token not in operands:
                my_stack.append((int(token)))
            else:
                result = 0
                first_num = my_stack.pop()
                second_num = my_stack.pop()
                if token == '+':
                    result = first_num + second_num
                elif token == '-':
                    result = second_num - first_num
                elif token == '*':
                    result = first_num * second_num
                else:
                    result = int(second_num / first_num)
                my_stack.append(result)
        return int(my_stack.pop())
                     