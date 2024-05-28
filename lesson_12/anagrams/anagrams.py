s1 = "cinema"
s2 = "iceman"

char_list_1 = list(s1)
char_list_2 = list(s2)

char_count = {}

for char in char_list_1:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for char in char_list_2:
    if char not in char_count:
        print("The strings are not anagrams.")
        break
    char_count[char] -= 1

for count in char_count.values():
    if count != 0:
        print("The strings are not anagrams.")
        break
else:
    print("The strings are anagrams.")
