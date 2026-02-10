def two_sum(nums, target):
    dict = {}
    for num in nums:
        dict[num] = True

    for num in nums:
        key_num = target - num
        # O(1)
        if key_num in dict and num != key_num:
            return True
        # if key_num in nums: O(n)
    return False


print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
print(two_sum([2, 1, 5, 7], 4))


