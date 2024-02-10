
if __name__ == '__main__':
    N = int(input())
    results = []
    phonebook = {}
    for i in range(N):
        name, phonNumber = input().split(" ")
        phonebook[name] = phonNumber

    for _ in range(N):
        friendName = input()

        if friendName in phonebook:
            results.append(friendName + "=" + phonebook.get(friendName))
        else:
            results.append("Not found")
    print("\n".join(results))



