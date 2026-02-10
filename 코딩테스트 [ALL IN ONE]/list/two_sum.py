# 직관적으로 생각하기 - 완전탐색

def two_sum(nums, target):
    n = len(nums)
    # O(n^2)
    ## O(n)
    for i in range(n-1):
        ## O(n)
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

print(two_sum(nums = [2,1,5,7], target=4))
