class AuthenticationManager:

    def __init__(self, timeToLive: int):  # O(1)
        self.time = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:  # O(1)
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None: # O(1)
        if tokenId in self.tokens and self.tokens[tokenId] + self.time > currentTime:
            self.tokens[tokenId] = currentTime
        elif tokenId in self.tokens:
            del self.tokens[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int: # O(N)
        count = 0
        for t in self.tokens:
            if self.tokens[t] + self.time > currentTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)