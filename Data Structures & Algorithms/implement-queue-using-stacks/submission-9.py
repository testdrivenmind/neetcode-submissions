class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        

    def push(self, x: int) -> None:
       
        self.input_stack.append(x)
        

    def pop(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                removed = self.input_stack.pop()
                self.output_stack.append(removed)
            return self.output_stack.pop()
        return self.output_stack.pop()
        

    def peek(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                removed = self.input_stack.pop()
                self.output_stack.append(removed)
            last = len(self.output_stack) - 1
            return self.output_stack[last]

        last = len(self.output_stack) - 1
        return self.output_stack[last]
            
    
       


        

    def empty(self) -> bool:
        return len(self.output_stack) == 0 and len(self.input_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()