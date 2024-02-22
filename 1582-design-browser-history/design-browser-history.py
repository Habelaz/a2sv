class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.forwardd = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.forwardd = []

    def back(self, steps: int) -> str:
        while steps and len(self.stack)>1:
            self.forwardd.append(self.stack.pop())
            steps -=1
        return self.stack[-1] 

    def forward(self, steps: int) -> str:
        while steps and len(self.forwardd) >0 :
            self.stack.append(self.forwardd.pop())
            steps -=1
        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)