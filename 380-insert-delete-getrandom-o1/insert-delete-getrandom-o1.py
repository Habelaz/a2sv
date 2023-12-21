class RandomizedSet:

    def __init__(self):
        self.val_ind = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_ind:
            return False

        self.values.append(val)
        self.val_ind[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_ind:
            return False

        last_val = self.values[-1]
        ind_remove = self.val_ind[val]
        self.values[ind_remove], self.values[-1] = self.values[-1], self.values[ind_remove]
        self.val_ind[last_val] = ind_remove
        del self.val_ind[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()