class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin  = celsius +273.15
        fahren = celsius * 1.8 + 32.00
        return [kelvin,fahren]