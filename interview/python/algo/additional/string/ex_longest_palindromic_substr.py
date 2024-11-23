# Given a string s, find the longest palindromic substring in s.
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Reference:
# https://leetcode.com/problems/longest-palindromic-substring/


def lps(s):
    if s is None or len(s) == 0:
        return ""

    l = len(s)
    start = 0
    max_len = 0

    for i in range(l):
        # for even len substr
        low = i-1
        high = i
        while low >= 0 and high < l and s[low] == s[high]:
            temp = high-low+1
            if temp >= max_len:
                start = low
                max_len = temp
            low -= 1
            high += 1

        # for odd len substr
        low = i-1
        high = i+1

        while low >= 0 and high < l and s[low] == s[high]:
            temp = high-low+1
            if temp >= max_len:
                start = low
                max_len = temp
            low -= 1
            high += 1

    if max_len == 0:
        return s[0]

    return s[start:start+max_len]

print (lps("babad")) # aba or bab
print (lps("cbbd")) # bb
print (lps("aba")) # aba
print (lps("bb")) # bb
