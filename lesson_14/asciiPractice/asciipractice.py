# Write a function that takes in a string of lowercase letters and an integer list of the same length. The function should shift all the letters in the string along the alphabet x number of times based on each integer in the list. If you shift 'a' once it will become 'b' and so forth. If you shift 'z' once it must wrap around to become 'a'.

# Two important points:
# 1. You must use ASCII values in some way to solve this challenge
# 2. Every letter in the string must be shifted by it's corresponding index value in the list and every integer that follows it. This is a bit tricky so I'll give an example.

# Example 1:
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

# Example2:
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"


def shift_all(str, shift):
    # str_array = [0 for i in range(len(str))]
    str_array = list(str)
    print(f"Str_Array: {str_array}")
    # for char in str:
    #     ascii = ord(char)
    #     _chr = chr(ascii)
    #     print(f"{char} to ascii ==> {ascii}")
    #     print(f"{ascii}+9 ==> {ascii+9} to ascii ==> {chr(ascii+9)}")

    for i in range(len(shift)):
        for j in range(i + 1):
            ascii = ord(str_array[j])
            # print(f"{str[j]} ==> {ascii}")
            print(f"{str_array[j]} ==> {ascii}")
            num = shift[i]
            new_ascii = ascii + num
            str_array[j] = convert(new_ascii)
            print(f"{ascii} + {num} = {new_ascii} ==> {str_array[j]}")
            print(f"STR_ARRAY: {str_array}")
        print("------")


def convert(num):
    if num > 122:
        diff = num - 122
        new_val = 97 + (diff - 1)
        return chr(new_val)
    else:
        return chr(num)


# print(convert(130))

s = "abc"
t = "xyz"
shifts = [3, 5, 9]
# print(shift_all("abc", [3, 5, 9]))


# Example2:
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
print(shift_all("aaa", [1, 2, 3]))
# print(shift_all(t, shifts))
# Input: s = "aaa", shifts = [1,2,3]
