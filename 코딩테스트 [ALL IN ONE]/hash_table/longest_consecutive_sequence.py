def longest_consecutive_sequence(nums):
    if len(nums) < 1:
        return 0
    
    longest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = 1

    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


## sort, 중복제거 풀이 방법

# def longest_consecutive_sequence(nums):
#     if len(nums) < 1:
#         return 0
    
#     nums = list(set(nums))
#     nums_dict = {}
#     nums.sort()
#     count = 1
#     max_count = 1

#     for num in nums:
#         nums_dict[num] = 1

#     for num in nums:
#         if num + 1 in nums_dict:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             count = 1

#     return max_count



def longest_consecutive_sequenc_aa(nums):
    if len(nums) < 1:
        return 0
    nums_dict = {}
    count = max_count = 1

    for num in nums:
        nums_dict[num] = 1

    for num in sorted(nums_dict):
        if num + 1 in nums_dict:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1

    return max(max_count, count)

# print(longest_consecutive_sequenc_aa([100, 4, 200, 1, 3, 2]))
# print(longest_consecutive_sequenc_aa([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longest_consecutive_sequenc_aa([1,0,-1]))

    

        
    