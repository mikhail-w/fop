def bubbleSortCount(arr):
    sorted = False
    comparisons = 0
    exchanges = 0

    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                exchanges += 1
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return (comparisons, exchanges)


print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7]))  # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4]))  # (10, 4)
