class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            new_row = []
            for j in range(len(strs)):
                new_row.append(strs[j][i])
            if new_row != sorted(new_row):
                count += 1
        return count

