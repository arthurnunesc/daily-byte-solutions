# This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

import string


def check_palyndrome(word):
    word = word.lower().replace(" ", "").translate(str.maketrans("", "", string.punctuation))
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False

print(check_palyndrome("Level"))
print(check_palyndrome("algorithm"))
print(check_palyndrome("ararA"))
print(check_palyndrome("LMAO"))
print(check_palyndrome("A man, a plan, a canal: Panama."))