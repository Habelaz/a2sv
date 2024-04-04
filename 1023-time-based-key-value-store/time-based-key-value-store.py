class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        ans = ''
        temp = self.d[key]

        low,high = 0,len(temp) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # if temp[mid][1] == timestamp:
            #     return temp[mid][0]
            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)