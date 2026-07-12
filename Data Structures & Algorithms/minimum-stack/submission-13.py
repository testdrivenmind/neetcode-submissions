class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val
            self.stack.append((val, min_val))
        else:
            if val < self.stack[-1][1]:
                self.stack.append((val, val))
            else:
                min_val = self.stack[-1][1]
                self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()[0]
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
