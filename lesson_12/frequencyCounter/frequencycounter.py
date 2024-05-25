def same(l1, l2):
    if len(l1) != len(l2):
        return False
    l1_count = {}
    l2_count = {}

    for val in l1:
        if val not in l1_count:
            l1_count[val] = 1
        else:
            l1_count[val] += 1

    for val in l2:
        if val not in l2_count:
            l2_count[val] = 1
        else:
            l2_count[val] += 1

    for key in l1_count:
        if key**2 not in l2_count:
            return False
        if l1_count[key] != l2_count[key**2]:
            return False

    return True


print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 1], [4, 4, 1]))
