# 5. One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# prt, pbdls -> false


from helper import Test


def one_away(s1, s2):
    if len(s2) > len(s1):
        return one_away(s2, s1)

    if len(s1) - len(s2) > 1:
        return False

    if len(s1) == len(s2):
        return one_replace_check(s1, s2)

    return one_insert_check(s1, s2)


def one_replace_check(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = not edited

    return True


def one_insert_check(s1, s2):
    edited = False
    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
        else:
            j += 1
        i += 1

    if edited and i < len(s1) or j < len(s2):
        return False

    return True


data = [
    {
        "input": ["pale", "ple"],
        "output": True,
    },
    {
        "input": ["pales", "pale"],
        "output": True,
    },
    {
        "input": ["pale", "bale"],
        "output": True,
    },
    {
        "input": ["pale", "bake"],
        "output": False,
    },
    {
        "input": ["prt", "pbdls"],
        "output": False,
    },
    {
        "input": ["palea", "paleaa"],
        "output": True,
    },
    {
        "input": ["palea", "kale"],
        "output": False,
    },
    {
        "input": ["pale", "paleee"],
        "output": False,
    }
]

test = Test()
test.check(one_away, data)
