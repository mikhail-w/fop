alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = input("Enter word: ").upper()
# print(word)
# print(f"Word length: {len(word)}")
dict = {}
for i in word:
    if i in alpha:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
print(dict)
