class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
            self.stack.append((val, current_min))
            return
        current_min = min(self.stack[-1][1], val)
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
