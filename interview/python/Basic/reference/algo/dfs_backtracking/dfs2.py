# LC22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# Eg-1,
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Eg-2,
# Input: n = 1
# Output: ["()"]


def generateParenthesis(n):
        if n < 0:
            return []
        
        if n == 0:
            return ['()']
        
        res = []
        
        dfs(n, 0, 0, "", res)
        return res
    

def dfs(n, open, close, curr, res):
    if len(curr) == n*2:
        res.append(curr)
        return
    
    if open < n:
        dfs(n, open+1, close, curr+'(', res)
    
    if close < open:
        dfs(n, open, close+1, curr+')', res)
    
    return



print(generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"])
