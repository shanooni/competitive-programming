"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""


def split_join(s: str):
    split_and_join = s.split(" ")
    split_and_join = "-".join(split_and_join)
    return split_and_join


print(split_join("this is a string"))


"""
output
this-is-a-string
"""