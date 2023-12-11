class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)/4
        my_dict = Counter(arr)
        for i,l in my_dict.items():
            if l > n:
                return i