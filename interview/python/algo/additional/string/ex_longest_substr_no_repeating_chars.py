# Longest Substring Without Repeating Characters
#
# Example 1,
# Input: "abcabcbb"
# Output: "abc"
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2,
# Input: "bbbbb"
# Output: "b"
# Explanation: The answer is "b", with the length of 1.
#
# Example 3,
# Input: "pwwkew"
# Output: "wke"
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Reference:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def longest_substr_no_repeating_chars(s):
    s_len = len(s)
    if s_len < 2:
        return s

    start = 0

    start_substr = 0
    end_substr = 0

    longest_substr = float('-inf')

    visited_char = {}

    for end in range(s_len):
        temp = s[end]
        if temp in visited_char:
            start = max(start, visited_char[temp] + 1)
            visited_char[temp] = end
        else:
            visited_char.update({temp: end})
        if longest_substr < (end-start+1):
            start_substr = start
            end_substr = end
            longest_substr = end_substr - start_substr + 1

    if longest_substr < (end-start+1):
        start_substr = start
        end_substr = end
        longest_substr = end_substr - start_substr + 1

    print ("Length of longest substring without repeating chars:", longest_substr)

    return s[start_substr:end_substr+1]


print (longest_substr_no_repeating_chars("abcabcbb")) # abc
print (longest_substr_no_repeating_chars("bbbbb")) # b
print (longest_substr_no_repeating_chars("pwwkew")) # wke or kew



# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1,
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2,
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3,
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Reference:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/



def length_of_longest_substring(s):
    if len(s) < 2:
        return len(s)

    start = 0

    visited_char = {}

    max_ls = float('-inf')

    str_len = len(s)
    for end in range(str_len):
        if s[end] in visited_char:
            start = max(start, visited_char[s[end]] + 1)
            visited_char[s[end]] = end
        else:
            visited_char.update({s[end] : end})

        max_ls = max(max_ls, end-start+1)
    return max_ls

print (length_of_longest_substring("abcabcbb")) # 3
print (length_of_longest_substring("bbbbb")) # 1
print (length_of_longest_substring("pwwkew")) # 3
