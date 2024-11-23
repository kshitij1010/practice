# 4. Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)


def ifPalindromePermutation(s):
    if s is None or len(s) <= 0:
        return True

    char_tracker = dict()

    for c in s:
        if c.isspace():
            continue

        c = c.lower()
        if c in char_tracker:
            char_tracker[c] += 1
        else:
            char_tracker[c] = 1

    odd_count = False
    for _, v in char_tracker.items():
        if v%2 != 0 :
            if odd_count:
                return False
            odd_count = True

    return True



data = [
        {
            "input": ["Tact Coaoo"], 
            "output": True,
        },
        {
            "input": ["Tact Coa"], 
            "output": True,
        },
        {
            "input": ["Tact! Coa!"], 
            "output": True,
        },
        {
            "input": ["hyehhhhyeh"], 
            "output": True,
        },
        {
            "input": ["hello world!"], 
            "output": False,
        },
        {
            "input": [""], 
            "output": True,
        },
        {
            "input": ["%^&)&%^"], 
            "output": True,
        },
        {
            "input": ["aabcddcbbacdadc"], 
            "output": True,
        }
    ]


from helper import Test
test = Test()
test.check(ifPalindromePermutation, data)
