# Reverse an array without affecting special characters
#
# Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’),
# reverse the string in a way that special characters are not affected.
#
# Reference:
# https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/


def reverse_word(s):
    l = 0
    r = len(s) - 1

    s_list = list(s)

    while l < r:
        if s_list[l].isalpha() and s_list[r].isalpha():
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        elif s_list[l].isalpha():
            r -= 1
        else:
            l += 1
    res = ''.join(s_list)
    return res


s1 = "Ab,c,de!$"
print (reverse_word(s1))


s2 = "a,b$c"
print (reverse_word(s2))


# Since the string in python is immutable, we are converting the string to the list and at the end list to the string
