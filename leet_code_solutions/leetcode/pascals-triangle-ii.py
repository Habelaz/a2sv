class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(rowIndex):
            if rowIndex <= 0:
                return [1]
            prev = pascal(rowIndex - 1)
            current = [1]

            for i in range(1,len(prev)):
                current.append(prev[i-1]+prev[i])
            current.append(1)

            return current
        return pascal(rowIndex)
            
        

            