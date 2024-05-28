def maxSubListSum(arr, num):
    if len(arr) < num:
        return None
    left = 0
    right = num - 1
    max_sum = 0

    while right < len(arr):
        sum_ = sum(arr[left : right + 1])
        if sum_ > max_sum:
            max_sum = sum_
        left += 1
        right += 1
    return max_sum


print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2))  # 10
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4))  # 17
print(maxSubListSum([4, 2, 1, 6], 1))  # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4))  # 13
print(maxSubListSum([], 4))  # None
