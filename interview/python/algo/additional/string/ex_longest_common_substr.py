# print Longest common substring
#
# Reference:
# https://www.youtube.com/watch?v=BysNXJHzCEs

def longest_common_substr(s1, s2):
    if s1 is None or len(s1) < 1 or s2 is None or len(s2) < 1:
        print ("One of the string is empty")
        return ""

    s1_len = len(s1)
    s2_len = len(s2)
    max_char_count = 0
    row = 0
    col = 0

    L = [ [0]*(s2_len+1) for k in range(s1_len+1) ]

    for i in range(s1_len+1):
        for j in range(s2_len+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                if max_char_count < L[i][j]:
                    max_char_count = L[i][j]
                    row = i
                    col = j
            else:
                L[i][j] = 0

    lcs = []
    while row > 0 and col > 0 and L[row][col] != 0:
        lcs.append(s1[row-1])
        row -= 1
        col -= 1

    # print ("length of longest_common_substr:", max_char_count)
    return "".join(lcs[::-1])


print (longest_common_substr("GeeksforGeeks", "GeeksQuiz")) # 5, Geeks
# assert longest_common_substr("GeeksforGeeks", "GeeksQuiz") == "Geeks", "Wrong!!!!!!"
print (longest_common_substr("abcdxyz", "xyzabcd")) # 4, abcd
print (longest_common_substr("zxabcdezy", "yzabcdezx")) # 6, abcdez
print (longest_common_substr("abcdaf", "zbcdf")) # 3, bcd
print (longest_common_substr("", "zbcdf")) # 0,
print (longest_common_substr("abcdaf", "")) # 0,
print (longest_common_substr("abcdefghi", "mnopqrst")) # 0,


import unittest


class TestMethod(unittest.TestCase):

    def test_lcs1(self):
        self.assertEqual(longest_common_substr("GeeksforGeeks", "GeeksQuiz"), "Geeks", "Wrong1!!!!!!")

    @unittest.expectedFailure
    def test_lcs2(self):
        self.assertEqual(longest_common_substr("abcdxyz", "xyzabcd"), "abacd", "Wrong2!!!!!!")

    @unittest.skip("No reason for skipping so just testing the skip")
    def test_lcs3(self):
        self.assertEqual(longest_common_substr("zxabcdezy", "yzabcdezx"), "abcdez", "Wrong3!!!!!!")

    def test_lcs4(self):
        self.assertEqual(longest_common_substr("abcdefghi", "mnopqrst"), "", "Wrong4!!!!!!")


unittest.main(verbosity=2)
