if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input().split()
        if command[0].lower() == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0].lower() == "remove":
            lst.remove(int(command[1]))
        elif command[0].lower() == "append":
            lst.append(int(command[1]))
        elif command[0].lower() == "pop":
            lst.pop()
        elif command[0].lower() == "sort":
            lst.sort()
        elif command[0].lower() == "reverse":
            lst.reverse()
        elif command[0].lower() == "print":
            print(lst)

