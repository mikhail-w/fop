while True:
    amount = int(input("Please enter an amount in cents less than a dollar."))
    if 0 <= amount <= 99:
        Q = amount // 25
        print(f"Q: {Q}")
        remainder = amount % 25
        # print(f"Remainder: {remainder}")
        D = remainder // 10
        print(f"D: {D}")
        remainder = remainder % 10
        # print(f"Remainder: {remainder}")
        N = remainder // 5
        print(f"N: {N}")
        remainder = remainder % 5
        # print(f"Remainder: {remainder}")
        print(f"P: {remainder}")
        break
    else:
        print("This is not a valid amount.")
