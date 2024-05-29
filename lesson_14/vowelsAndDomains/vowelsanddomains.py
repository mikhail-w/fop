# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']


# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']

import re


def start_vowels(str):
    arr = str.split(" ")
    res = []
    regex = "^[aeiou]"
    regex2 = r"\b^[aeiou][a-z]*\b"
    for word in arr:
        if re.search(regex, word, re.IGNORECASE):
            res.append(word)

    return res


print(start_vowels("Errors should never pass silently. Unless explicitly silenced."))
