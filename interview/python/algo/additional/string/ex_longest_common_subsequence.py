# print Longest common subsequence
# 
# Reference:
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/


def print_longest_common_subsequence(s1, s2):
    if s1 is None or len(s1) == 0:
        return "String1 missing, No LCS found"

    if s2 is None or len(s2) == 0:
        return "String2 missing, No LCS found"

    s1_len = len(s1)
    s2_len = len(s2)

    L = [ [0]*(s2_len+1) for k in range(s1_len+1) ]

    for i in range(s1_len+1):
        for j in range(s2_len+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: # since string starts from 0 and we did not match tha when i or j is zero so we did i-1 and j-1
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    lcs = []

    i = s1_len
    j = s2_len

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    if len(lcs) < 1:
        return "No LCS found"

    return "".join(lcs[::-1])


def print_res(s1, s2, expected):
    print ("\n\ninput: " + s1 +", " + s2)
    print ("Expected output:", expected)

    print ("Actual output:", print_longest_common_subsequence(s1, s2))



print_res("ABCDGH", "AEDFHR", "ADH")
print_res("", "hit", "")
print_res("neat", "", "")
print_res("heat", "hit", "ht")
print_res("awesome", "awesome", "awesome")
print_res("abc", "adbc", "abc")
print_res("some", "thing", "")
print_res("AGGTAB", "GXTXAYB", "GTAB")



# ************************ Similar question **************************
# Deletion Distance
#
# The deletion distance of two strings is the minimum number of characters you need to delete in the two strings
# in order to get the same string.
#
# For instance, the deletion distance between "heat" and "hit" is 3:
#
# By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
# We cannot get the same string from both strings by deleting 2 letters or fewer.
# Given the strings str1 and str2, write an efficient function deletionDistance that
# returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.
#
# Example,
# input:  str1 = "dog", str2 = "frog"
# output: 3
#
# input:  str1 = "some", str2 = "some"
# output: 0
#
# input:  str1 = "some", str2 = "thing"
# output: 9
#
# input:  str1 = "", str2 = ""
# output: 0
#
# Reference:
# https://www.pramp.com/challenge/61ojWAjLJbhob2nP2q1O
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/


def deletion_distance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    L = [[0] * (str2_len+1) for k in range(str1_len+1)]

    for i in range(str1_len + 1):
        for j in range(str2_len + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    lcs_len = 2 * L[-1][-1]
    return str1_len + str2_len - lcs_len


print ("\n\n\nQuestion 2: Deletion distance")
print ("Expected: 3,", "Actual:", deletion_distance("", "hit"))
print ("Expected: 4,", "Actual:", deletion_distance("neat", ""))
print ("Expected: 3,", "Actual:", deletion_distance("heat", "hit"))
print ("Expected: 2,", "Actual:", deletion_distance("hot", "not"))
print ("Expected: 9,", "Actual:", deletion_distance("some", "thing"))
print ("Expected: 1,", "Actual:", deletion_distance("abc", "adbc"))
print ("Expected: 0,", "Actual:", deletion_distance("awesome", "awesome"))
print ("Expected: 2,", "Actual:", deletion_distance("ab", "ba"))
