def bubbleSort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print(bubbleSort([5, 3, 10, 6, 1]))  # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10]))  # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4]))  # [0, 1, 2, 4, 5]

# Time Complexity O(n^2)
# Space Complexity O(1)
