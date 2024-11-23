# 9. String Rotation: Assume you have a method isSubstring which checks ifone word is asubstring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g.,"waterbottle"is a rotation of"erbottlewat").


def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False


def ifStrRotation(s1, s2):
    if len(s1) != len(s2):
        return False

    helper_string = s1 + s1

    return isSubstring(helper_string, s2)

data = [
        {
            "input": ["hlliohe","hi"], 
            "output": False,
        },
        {
            "input": ["abc","bca"], 
            "output": True,
        },
        {
            "input": ["abc","xyz"], 
            "output": False,
        },
        {
            "input": ["hello world!"," world!hello"], 
            "output": True,
        },
        {
            "input": ["abcdabcdabcd","hi"], 
            "output": False,
        },
        {
            "input": ["hey","h ey"], 
            "output": False,
        },
        {
            "input": ["hey","abc"], 
            "output": False,
        },
        {
            "input": ["    & ","&     "], 
            "output": True,
        },
        {
            "input": ["1234@#","@#1234"], 
            "output": True,
        },
        {
            "input": ["1234#@","@#1234"], 
            "output": False,
        },
    ]


from helper import Test
test = Test()
test.check(ifStrRotation, data)
