class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n=num1
        n=int(n)
        n1=num2
        n1=int(n1)

        return str(n+n1)