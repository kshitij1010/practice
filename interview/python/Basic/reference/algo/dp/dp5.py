# LC139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# https://leetcode.com/problems/word-break/
# Eg-1,
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Eg-2,
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Eg-3.py
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false


def wordBreak(s, wordDict):
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        max_len = 0
        
        for word in wordDict:
            max_len = max(max_len, len(word))
        
        for i in range(1,len(s)+1):
            for j in range(i,-1,-1):
                if j-i <= max_len:
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = True
                        break
                    
        return dp[-1]
