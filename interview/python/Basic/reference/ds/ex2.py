# 2. Check Permutation: Given two strings, write a method to decide if one is a permutation of the other Meaning two strings have same char in different orders



def if_permutation(s1, s2):
    if s1 is None or s2 is None:
        return False

    chars = dict()

    for c in s1:
        if c in chars:
            chars[c] +=1
        else:
            chars[c] = 1

    for c in s2:
        if c in chars:
            if chars[c] == 1:
                del chars[c]
            else:
                chars[c] -= 1

    if len(chars) > 0:
        return False

    return True



data = [
        {
            "input": ["hlliohe", "hi"], 
            "output": False,
        },
        {
            "input": ["hello world!", "world !hello"], 
            "output": True,
        },
        {
            "input": ["abcdabcdabcd", "hi"], 
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
            "input": ["1@#","@1#"], 
            "output": True,
        },

    ]


from helper import Test
test = Test()
test.check(if_permutation, data)
