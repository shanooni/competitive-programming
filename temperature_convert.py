"""
You are given a non-negative floating point number rounded to two decimal places celsius,
that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00
"""
from typing import List


def convert_temperature(celsius: int) -> List[float]:
    answer: List[float] = []
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    answer.append(kelvin)
    answer.append(fahrenheit)
    return answer


print(convert_temperature(35.50))
