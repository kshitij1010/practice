# LC17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Eg-1,
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Eg-2,
# Input: digits = ""
# Output: []
# Eg-3,
# Input: digits = "2"
# Output: ["a","b","c"]






def letterCombinations(digits):
    if digits is None or len(digits)==0:
        return []
    
    res = []
    
    mapping =   [
                    "0",
                    "1",
                    "abc",
                    "def",
                    "ghi",
                    "jkl",
                    "mno",
                    "pqrs",
                    "tuv",
                    "wxyz"
                
                ]
    
    combi(digits, 0, "", mapping, res)
    
    return res

def combi(digits, curr, combi, mapping, res):
    if curr == len(digits):
        res.append(combi)
        return
    
    curr_num = int(digits[curr])
    
    for c in mapping[curr_num]:
        combi(digits, curr+1, combi+c, mapping, res)
        
    return
    