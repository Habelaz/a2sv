class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n1=num1
        n1=int(n1)
        n2=num2
        n2=int(n2)

        return str(n1*n2)