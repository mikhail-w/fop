def get_sum(li):
    sum = 0
    for num in li:
        sum += num
    return sum


li = [1, 2, 3, 4, 5]

total = get_sum(li)
total2 = sum(li)
print(total)
print(total2)
