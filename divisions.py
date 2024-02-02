"""
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // .
The second line should contain the result of float division,  / .
No rounding or formatting is necessary.
"""


def div(a: int, b: int):
    floor_div = a // b
    simple_div = a / b
    print(floor_div)
    print(simple_div)


div(3, 5)

"""
output: 
0
0.6
"""
