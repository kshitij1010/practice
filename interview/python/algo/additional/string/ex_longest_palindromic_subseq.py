# Longest Palindromic Subsequence
#
# Given a sequence, find the length of the longest palindromic subsequence in it
#
# Reference:
# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# https://www.youtube.com/watch?v=_nCsPn7_OgI&t=59s&ab_channel=TusharRoy-CodingMadeSimple
# https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestPalindromicSubsequence.java


def longestPalindromicSubSeq(s):
    start = 0
    end = len(s)-1

    return helper(s, start, end)

def helper(s, start, end):
    if start >= end:
        return 1

    if s[start] == s[end]:
        return 2 + helper(s, start+1, end-1)
    else:
        return max(helper(s, start, end-1), helper(s, start+1, end))

s = "agfgaa"
print (longestPalindromicSubSeq(s))
