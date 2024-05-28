def sumZero(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        pair_sum = arr[left] + arr[right]
        if pair_sum == 0:
            return [arr[left], arr[right]]
        elif pair_sum > 0:
            right -= 1
        else:
            left += 1

    return -1


print(sumZero([-3, -2, -1, 0, 1, 2, 3]))
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99]))
