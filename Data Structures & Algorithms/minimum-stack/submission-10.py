class MinStack:

    def __init__(self):
        self.my_stack = []


    def push(self, val: int) -> None:
        if not self.my_stack:
            current_min = val
            self.my_stack.append((val, current_min))
            return 
        current_min = self.my_stack[-1][1]
        if val < current_min:
            current_min = val
        self.my_stack.append((val, current_min))

    def pop(self) -> None:
        if self.my_stack:
            self.my_stack.pop()

        

    def top(self) -> int:
        if self.my_stack:
            return self.my_stack[-1][0]
        return 0

    def getMin(self) -> int:
        if self.my_stack:
            return self.my_stack[-1][1]
        return 0
