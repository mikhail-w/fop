def double(n):
    t = 0
    for i in range(n):
        t += 2
        print(t, end=" ")
    print()
    return t


print(double(5))
