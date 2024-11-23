# Wildcard matching
#
# Reference:
# https://www.youtube.com/watch?v=3ZDZ-N0EPV0


def if_wildcard_match(s, p):
    if set(p) == set('*'):
        return True
    
    len_s = len(s)
    len_p = len(p)
    
    dp = [[False]*(len_p+1) for j in range(len_s+1)]
    dp[0][0] = True

    for j in range(1,len_p):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    for i in range(1, len_s+1):
        for j in range(1, len_p+1):
            if p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    
    return dp[-1][-1]


def print_res_for_wildcard_match(text, pattern, expected):
    print ("\nInput => Text:", text, "Pattern:", pattern, "Expected:", expected)
    print ("Output =>", if_wildcard_match(text, pattern))
    return

print_res_for_wildcard_match("xbylmz", "x?y*z", True)
print_res_for_wildcard_match("xblmz", "x?y*z", False)
print_res_for_wildcard_match("aq", "?q", True)
print_res_for_wildcard_match("axyb", "a*b", True)
print_res_for_wildcard_match("xqwerty", "*", True)
print_res_for_wildcard_match("xqwerty", "*?", True)
print_res_for_wildcard_match("xbylmz", "?*", True)
print_res_for_wildcard_match("xqwertya", "*?a", True)
print_res_for_wildcard_match("xqwerty", "*?a", False)
print_res_for_wildcard_match("aa", "?", False)
