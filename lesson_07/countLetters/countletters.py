def count_letters(word):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}

    for i in word:
        if i in alpha:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

    # print(dict)
    return dict


word = input("Enter word: ").upper()
print(count_letters(word))
