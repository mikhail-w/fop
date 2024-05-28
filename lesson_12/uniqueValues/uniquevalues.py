def countUniqueValues(arr):
    if not arr:
        return 0
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 0
        count[num] += 1

    return len(count)


print(countUniqueValues([1, 1, 1, 1, 1, 2]))  # 2
print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))  # 7
print(countUniqueValues([-2, -1, -1, 0, 1]))  # 4
print(countUniqueValues([]))  # 0
