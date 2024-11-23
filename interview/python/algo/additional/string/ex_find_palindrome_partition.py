# Given a string, print all possible palindromic partitions
# Given a string, find all possible palindromic partitions of given string.
# Example,
# Input   : "nitin"
# Output  : n i t i n
#           n iti n
#           nitin
# Input    : "geeks"
# Output   : g e e k s
#            g ee k s
#
# Reference:
# https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
# https://statyang.wordpress.com/python-practice-83-palindrome-partitioning/


def is_palindrome(s):
	return s == s[::-1]


def find_palindrome(s, palin_list, res):
	if len(s) == 0:
		res.append(palin_list)
		return

	for i in range(1,len(s)+1):
		if is_palindrome(s[:i]):
			find_palindrome(s[i:], palin_list + [s[:i]], res)


def find_palindromic_partition_substr_list(s):
	res = []
	find_palindrome(s, [], res)
	return res


s1 = "nitin"
print (find_palindromic_partition_substr_list(s1))
# output: [['n', 'i', 't', 'i', 'n'], ['n', 'iti', 'n'], ['nitin']]

s2 = "geeks"
print (find_palindromic_partition_substr_list(s2))
# output: [['g', 'e', 'e', 'k', 's'], ['g', 'ee', 'k', 's']]

s3 = "aabac"
print (find_palindromic_partition_substr_list(s3))
# [['a', 'a', 'b', 'a', 'c'], ['a', 'aba', 'c'], ['aa', 'b', 'a', 'c']]
