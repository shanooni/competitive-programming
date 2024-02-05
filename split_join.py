"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""


def split_and_join(line: str) -> str:
    split = line.split(" ")
    join = "-".join(split)
    return join


if __name__ == '__main__':
    line = input()
    print(split_and_join(line))
