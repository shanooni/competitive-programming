def smallestNumber(num: int) -> int:
    strNum = str(num)
    n = len(strNum)
    strList = []
    for i in range(n):
        newStr = strNum[i]
        for j in range(n):
            print(f" for i : {strNum[i]} and j : {strNum[j]}")
            if strNum[j] not in newStr:
                newStr += strNum[j]
                print(newStr)
                strList.append(newStr)
    print(strList)


smallestNumber(-7605)
