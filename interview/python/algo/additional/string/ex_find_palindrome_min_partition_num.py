####################################################################################
# Follow up or Previous related question
#
# Given a string, print all possible palindromic partitions
# Given a string, find the min of possible palindromic partitions of given string.
# Example,
# Input   : "ababbbabbababa"   Exaplnation: "a" | "babbbab" | "b" | "ababa"
# Output  : 3
# Input    : "geeks"
# Output   : g e e k s
#            g ee k s
#
# Reference:
# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/


####### simple solution. (Not efficient)
def find_palindrome_partition_simple(s, count, min_count):
	if len(s) == 0:
		min_count[0] = min(count-1, min_count[0])
		return

	for i in range(1,len(s)+1):
		if is_palindrome(s[:i]):
			find_palindrome_partition_simple(s[i:], count+1, min_count)


def find_min_palindromic_partition_number_simple(s):
	min_count = [float('inf')]
	count = 0
	find_palindrome_partition_simple(s, count, min_count)
	return min_count[0]


####### Dynamic programming. (Optimized-efficient solution)
# Reference:
# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/221249/Python-Two-Pointers-%2B-DP-O(N2)
# https://www.youtube.com/watch?v=lDYIvtBVmgo
# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/137296/two-python-dp-solution-with-explaination

def find_min_palindromic_partition_number(s):
	len_s = len(s)
	cut = [float('inf')] * len_s
	is_pal = [[False] * len_s for _ in range(len_s)]

	for end in range(len_s):
		for start in range(len_s):
			if s[end] == s[start] and (start + 1 >= end or is_pal[start+1][end-1]):
				is_pal[start][end] = True
				if start == 0:
					cut[end] = 0
				else:
					cut[end] = min(cut[end], cut[start-1]+1)
	return cut[-1]


s1 = "nitin"
print (find_min_palindromic_partition_number(s1)) # 0

s2 = "geeks"
print (find_min_palindromic_partition_number(s2)) # 3

s3 = "aabac"
print (find_min_palindromic_partition_number(s3)) # 2

s4 = "ababbbabbababa"
print (find_min_palindromic_partition_number(s4))
# Output: 3

s5 = "abcbm"
print (find_min_palindromic_partition_number(s5))
# Output: 2
