from collections import defaultdict

if __name__ == '__main__':
    length_of_input = int(input())

    file_names = {}

    for _ in range(length_of_input):

        file_name = input()
        if file_name not in file_names:
            print("OK")
            file_names[file_name] = file_names.get(file_name, 1)
        else:
            print(f"{file_name}{file_names[file_name]}")
            file_names[file_name] += 1
