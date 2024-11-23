# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


from helper import Test


# Solution
def lengthOfLongestSubstring(self, s: str) -> int:
    start, longest = 0, 0
    seenChars = {}
    for i, c in enumerate(s):
        if c in seenChars:
            start = max(start, seenChars[c]+1)
            # delete dict until seenChars[c]
        longest = max(longest, i-start+1)
        seenChars[c] = i
    longest = max(longest, len(s)-start)
    return longest


# Start test
data = [
        {
            "input": "abcabcbb", 
            "output": 3,
        },
        {
            "input": "bbbbb", 
            "output": 1,
        },
        {
            "input": "pwwkew", 
            "output": 3,
        },
        {
            "input": "", 
            "output": 0,
        },
        {
            "input":"pwwkewr",
            "output": 4,
        },
        {
            "input":"tmmzuxt",
            "output": 5,
        },
        {
            "input":"alouzxilkaxkufsu",
            "output": 8,
        }
    ]


# Start test
test = Test()
test.check(lengthOfLongestSubstring, data)
