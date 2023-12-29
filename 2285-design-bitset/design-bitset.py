class Bitset:

    def __init__(self, size: int):
        self.sz = size
        self.bits = [False] * size
        self.flipped = [True] * size
        self.bitCount = 0
        
    def fix(self, idx: int) -> None:
        if not self.bits[idx]:
            self.bits[idx] ^= True
            self.flipped[idx] ^= True
            self.bitCount += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx]:
            self.bits[idx] ^= True
            self.flipped[idx] ^= True
            self.bitCount -= 1

    def flip(self) -> None:
        self.bits, self.flipped = self.flipped, self.bits
        self.bitCount = self.sz - self.bitCount    

    def all(self) -> bool:
        return self.sz == self.bitCount

    def one(self) -> bool:
        return self.bitCount > 0

    def count(self) -> int:
        return self.bitCount

    def toString(self) -> str:
        return ''.join(['1' if b else '0' for b in self.bits])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()