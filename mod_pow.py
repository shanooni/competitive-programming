"""
Task
You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains , the second line contains , and the third line contains .
"""


def mod_pow(a: int, b: int, m: int = None) -> float:
    expo = a ** b
    if m is not None:
        expo_mod = expo % m
        print(expo)
        print(expo_mod)
    else:
        print(expo)


mod_pow(3, 4, 5)

"""
output:
81
1
"""
