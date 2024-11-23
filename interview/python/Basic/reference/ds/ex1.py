# 1. Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


def is_unique(s):
    if s is None or len(s) <= 0:
        return False

    char_tacker = set()

    for c in s:
        if c in char_tacker:
            return False
        char_tacker.add(c)
    
    return True


def is_unique2(s):
    if s is None or len(s) <= 0:
        return False

    char_tracker = [0]*256

    for c in s:
        ascii_char = ord(c)
        if char_tracker[ascii_char] > 0:
            return False
        char_tracker[ascii_char] += 1

    return True


data = [
        {
            "input": "hello world", 
            "output": False,
        },
        {
            "input": "Heya  hbcd", 
            "output": False,
        },
        {
            "input": "abCdefGh", 
            "output": True,
        },
        {
            "input": "tT", 
            "output": True,
        },
        {
            "input": "!@#$%^", 
            "output": True,
        },
        {
            "input": "!@#$ %^", 
            "output": True,
        },
        {
            "input": "!@#$%^%", 
            "output": False,
        },
        {
            "input": "1234567", 
            "output": True,
        },
        {
            "input": "12341567", 
            "output": False,
        },
    ]


from helper import Test
test = Test()
test.check(is_unique, data)
test.check(is_unique2, data)
