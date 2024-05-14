def hailstone(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    counter = 0
    temp = num

    while temp != 1:
        if temp % 2 == 0:
            temp = temp // 2
        else:
            temp = temp * 3 + 1
        counter += 1
        print(temp, end=" ")

    print()

    return counter


answer = hailstone(3)
print(f"It took {answer} step(s)")
