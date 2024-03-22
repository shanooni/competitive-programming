def palidrome_riddle(s: str):
    first = 0
    last = len(s) - 1
    change = 0
    while first <= last:
        if s[first] != s[last]:
            s[last] = s[first]
            change += 1
            if palindrome(s):
                break
            first += 1
            last -= 1
    print(change)


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


print(palidrome_riddle('ananas'))
