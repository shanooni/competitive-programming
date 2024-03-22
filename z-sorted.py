def z_sort(nums: list[int]) -> list[int]:
    Zsort = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and nums[i] >= nums[i - 1]:
            print("even")
            Zsort.append(nums[i])
            print(nums[i])
        elif nums[i] <= nums[i - 1]:
            print("odd")
            print(nums[i])
            Zsort.append(nums[i])

    return Zsort


print(z_sort([1, 2, 2, 1]))
