# This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

def reverse_string_easy(string):
    return string[::-1]

def reverse_string_manually(string):
    string_as_a_list = list(string)
    reversed_string_as_a_list = []
    for i in range(len(string_as_a_list)):
        reversed_string_as_a_list.append(string_as_a_list[-1])
        string_as_a_list.pop(-1)

    return "".join(reversed_string_as_a_list)


print(reverse_string_easy("Cat")) # "taC"
print(reverse_string_manually("The Daily Byte")) # "etyB yliaD ehT"
print(reverse_string_manually("civic")) # "civic"
