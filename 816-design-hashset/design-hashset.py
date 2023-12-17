class MyHashSet:

    def __init__(self):
        self.sett = []

    def add(self, key: int) -> None:
        if key not in self.sett:
            self.sett.append(key)

    def remove(self, key: int) -> None:
        if key in self.sett:
            self.sett.remove(key)

    def contains(self, key: int) -> bool:
        return  key in self.sett


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)