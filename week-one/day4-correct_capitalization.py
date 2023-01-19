# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

def check_capitalization(phrase):
    if phrase == phrase.lower():
        return True
    elif phrase == phrase.upper():
        return True
    elif list(phrase)[0].isupper():
        for letter in list(phrase)[1:]:
            if letter.isupper():
                return False
        return True
    return False

print(check_capitalization("USA")) # True
print(check_capitalization("Calvin")) # True
print(check_capitalization("compUter")) # False
print(check_capitalization("coding")) # True