class OutOfRangeError(Exception):
    pass


user_input = int(input("Enter the integer: "))
try:
    if user_input == 1:
        print(f"User entered one")
    elif user_input == 2:
        print(f"User entered two")
    elif user_input == 3:
        print(f"User entered three")
    else:
        raise OutOfRangeError

except OutOfRangeError:
    print("That's not one of the allowed values!")
