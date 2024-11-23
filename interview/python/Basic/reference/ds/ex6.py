# 6. String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).


def stringCompression(s):
    if s is None or len(s) <= 1:
        return s

    compressed = ""
    str_len = len(s)
    same_char_count = 1

    for i in range(1, str_len):
        if s[i] == s[i-1]:
            same_char_count += 1
        else:
            compressed += s[i-1] + str(same_char_count)
            same_char_count = 1

    compressed += s[i] + str(same_char_count)

    if len(compressed) > str_len:
        return s

    return compressed
        



data = [
    {
        "input": "aabcccccaaa",
        "output": "a2b1c5a3",
    },
    {
        "input": "aabcccccaaab",
        "output": "a2b1c5a3b1",
    },
    {
        "input": "abcd",
        "output": "abcd",
    },
    {
        "input": "abcccccaaaddddd",
        "output": "a1b1c5a3d5",
    },
    {
        "input": "z",
        "output": "z",
    },
    {
        "input": "bb",
        "output": "b2",
    },
    {
        "input": "...asdsdsdsd",
        "output": "...asdsdsdsd",
    },
    {
        "input": "yyyyyyyyyyyyyyyyy",
        "output": "y17",
    },
    {
        "input": "",
        "output": "",
    },
]

from helper import Test
test = Test()
test.check(stringCompression, data)
