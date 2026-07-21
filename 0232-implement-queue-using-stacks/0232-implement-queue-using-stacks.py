class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        self.peekEl = -1
        

    def push(self, x: int) -> None:
        if not self.input:
            self.peekEl = x
        self.input.append(x)    
        

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()        
        

    def peek(self) -> int:
        if not self.output:
            return self.peekEl
        return self.output[-1]    
        

    def empty(self) -> bool:
        return not self.input and not self.output
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()