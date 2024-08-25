from fractions import Fraction
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions: list[str] = re.findall(r'[+-]?\d+/\d+', expression)
        result: Fraction = Fraction(0)
        for frac in fractions:
            result += Fraction(frac)
        return f"{result.numerator}/{result.denominator}"