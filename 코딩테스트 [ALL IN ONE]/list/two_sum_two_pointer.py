def two_sum(nums, target):
    # O(nlogn)
    nums.sort()
    left = 0
    right = len(nums) - 1
    # O(n)
    while left != right:
        if nums[left] + nums[right] > target:
            right = right - 1
        elif nums[left] + nums[right] < target:
            left = left + 1
        else:
            return True
    return False


print(two_sum(nums = [2,1,5,7], target=4))

print(two_sum(nums = [4, 1, 9, 7, 5, 3, 16], target=14))