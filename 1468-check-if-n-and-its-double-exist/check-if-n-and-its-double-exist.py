class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mapp = set()
        for num in arr:
            if num / 2 in mapp or num * 2 in mapp:
                return True
            mapp.add(num)
        return False