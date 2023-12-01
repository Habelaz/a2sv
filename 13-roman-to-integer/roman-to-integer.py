class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        myList=[]
        for c in s:
            myList.append(c)
        myList.reverse()
        total=0
        pre=0
        for i in myList:
            value=roman_dict[i]
            if value<pre:
                total -=value
            else:
                total +=value
            pre=value
        return total
