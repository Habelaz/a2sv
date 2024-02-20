class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []
    def push(self, val: int) -> None:
        if not self.minn:
            self.minn.append(val)
        elif self.minn[-1] >= val:
            self.minn.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minn[-1]:
            self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1] if self.minn else self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()