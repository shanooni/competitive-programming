length_of_list, target = map(int, input().split())

nums = list(map(int, input().split()))
nums_index_dict = {}
for i in range(length_of_list+1):
    nums_index_dict[nums[i]] = i+1
print(nums_index_dict)
