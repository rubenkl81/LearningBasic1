numbers = [1, 4, 3, 5, 6, 4, 7]


def cont_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count


print(cont_4(numbers))
