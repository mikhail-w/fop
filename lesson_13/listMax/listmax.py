def list_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        rest = list_max(arr[1:])
        return rest if rest > arr[0] else arr[0]


print(list_max([1, 2, 39, 4, 5, 6, 7, 8]))
