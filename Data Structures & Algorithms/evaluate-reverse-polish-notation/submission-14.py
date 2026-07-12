class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operators = ["*", "+", "-", "/"]

        for token in tokens:
            if token not in operators:
                num_stack.append(int(token))
            else:
                second_operand = num_stack.pop()
                first_operand = num_stack.pop()
                match token:
                    case "*":
                        num_stack.append(first_operand * second_operand)
                    case "+":
                        num_stack.append(first_operand + second_operand)
                    case "-":
                        num_stack.append(first_operand - second_operand)
                    case "/":
                        num_stack.append(int(first_operand / second_operand))
        return num_stack[-1]