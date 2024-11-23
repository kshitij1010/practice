# Write a recursive function for generating all permutations of an input string.
# Return them as a set.
#
# Reference:
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# https://www.interviewcake.com/question/python/recursive-string-permutations?course=fc1&section=dynamic-programming-recursion


def permutations_helper(s, l, r):
    if l == r:
        print ("".join(s))
        return

    for i in range(l, r):
            s[i], s[l] = s[l], s[i]
            permutations_helper(s, l+1, r)
            s[i], s[l] = s[l], s[i] # backtracking

    return


def permutations(s):
    len_s = len(s)
    if len_s == 0 or s is None:
        return

    if len_s == 1:
        print (s)
        return

    s1 = list(s)
    permutations_helper(s1, 0, len(s1))

permutations("ABC")
