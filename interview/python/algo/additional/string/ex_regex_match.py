# Basic Regex Parser
#
# Implement a regular expression function isMatch that supports the '.' and '*' symbols.
# The function receives two strings text & pattern and
# should return true if the text matches the pattern as a regular expression.
# For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string
# and are used as special symbols only in the pattern string.
#
# In case you aren’t familiar with regular expressions,
# the function determines if the text and pattern are the equal,
# where the '.' is treated as a single a character wildcard (see third example),
# and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples).
#
# Explain your algorithm, and analyze its time and space complexities.
#
# Examples,
#
# input:  text = "aa", pattern = "a"
# output: false
#
# input:  text = "aa", pattern = "aa"
# output: true
#
# input:  text = "abc", pattern = "a.c"
# output: true
#
# input:  text = "abbb", pattern = "ab*"
# output: true
#
# input:  text = "acd", pattern = "ab*c."
# output: true
#
# Reference:
# https://www.pramp.com/challenge/KvZ3aL35Ezc5K9Eq9Llp
# https://www.youtube.com/watch?v=l3hda49XcDE
# https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/RegexMatching.java

def if_regex_match(text, pattern):
    if set(pattern) == set('*'):
        return True

    len_t = len(text)
    len_p = len(pattern)

    # create 2 d array to store result in boolean form
	# M[i][j] is true if text[:i] matches pattern[:j] else false
    M = [[False]*(len_p+1) for i in range(len_t+1)]

    # empty string matches empty pattern, hence true
    M[0][0] = True

    # if pattern has pattern = "d*" and text = "" then compute the result for first row
    for j in range(1,len_p+1):
        if pattern[j-1] == "*":
            M[0][j] = M[0][j-2]

    # construct DP based on previous values
    for i in range(1, len_t+1):
        for j in range(1, len_p+1):
            # if there is a char match or pattern has '.' then copy result from i-1, j-1
            if pattern[j-1] == "." or text[i-1] == pattern[j-1]:
                M[i][j] = M[i-1][j-1]
            elif pattern[j-1] == "*":  # if char is '*' then
                if pattern[j-2] == "." or text[i-1] == pattern[j-2]:
                    # one occurance or multiple occurance or no occurence
                    M[i][j] = M[i][j-1] or M[i-1][j] or M[i][j-2]
                else:
                    M[i][j] = M[i][j-2]  # no occurence

    return M[-1][-1]

def print_res_for_regex_match(text, pattern, expected):
    print ()
    print ("Input => Text:", text, "Pattern:", pattern, "Expected:", expected)
    print ("Output =>", if_regex_match(text, pattern))
    return


print_res_for_regex_match("", "", True)
print_res_for_regex_match("aa", "a", False)
print_res_for_regex_match("bb", "bb", True)
print_res_for_regex_match("", "a*", True)
print_res_for_regex_match("a", "*abc", False)
print_res_for_regex_match("abbdbb", "ab*d", False)
print_res_for_regex_match("aba", "a.a", True)
print_res_for_regex_match("acd", "ab*c.", True)
print_res_for_regex_match("aba", "a.*a", True)
print_res_for_regex_match("ablma", "a.*a", True)
