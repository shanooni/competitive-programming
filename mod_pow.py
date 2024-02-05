"""
Task
You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains , the second line contains , and the third line contains .
"""


def mod_pow(a: int, b: int, m: int = None):
    expo = a ** b
    if m is not None:
        expo_mod = expo % m
        print(expo)
        print(expo_mod)
    else:
        print(expo)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    mod_pow(a, b, m)
