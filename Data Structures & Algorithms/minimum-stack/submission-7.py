class MinStack:

    def __init__(self):
        self.my_stack = []
        self.size = -1


    def push(self, val: int) -> None:
        if not self.my_stack:
            current_min = val
            self.my_stack.append((val, current_min))
            self.size += 1
        else:
            current_min = self.my_stack[self.size][1]
            if val < current_min:
                current_min = val
                self.my_stack.append((val, current_min))
                self.size += 1
            else:
                self.my_stack.append((val, current_min))
                self.size += 1

    def pop(self) -> None:
        if self.my_stack:
            self.my_stack.pop()
            self.size -= 1
        

    def top(self) -> int:
        if self.my_stack:
            return self.my_stack[self.size][0]
        return 0

    def getMin(self) -> int:
        if self.my_stack:
            return self.my_stack[self.size][1]
        return 0
