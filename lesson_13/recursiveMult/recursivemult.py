def multiply(n1, n2):
    if n2 == 1:
        return n1
    return n1 + multiply(n1, (n2 - 1))


print(multiply(3, 4))
