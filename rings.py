def rings_count(s: str):
    count = 0

    n = len(s) - 1
    if 'O' not in s:
        count
    else:
        count = 1
        for i in range(n):
            if s[i] == 'O' and s[i + 1] == 'O':
                count += 1
            elif s[i] == 'O' and s[i + 1] != '0':
                # reset count to zero
                break
    print(count)


rings_count('HHHHOOSO')  # 2
rings_count('SSSSOOOHSHHHO')  # 3
rings_count('HHSS')
rings_count('OOSSOOOH')  # 3
rings_count('OOOOOOOOO')
