if __name__ == "__main__":
    n = int(input())

    refStr = "abc"

    for _ in range(n):
        Str = input()

        if Str == refStr:
            print("Yes")
        elif Str[0] == 'a' or Str[1] == 'b' or Str[2] == 'c':
            print("Yes")
        else:
            print("No")
