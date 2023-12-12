class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.counter = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.arr[idKey] = value
        if self.counter < idKey:
            return []
        while self.counter < len(self.arr) and  self.arr[self.counter] != None:
            self.counter += 1
        return self.arr[idKey:self.counter]
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)