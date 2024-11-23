# 3. URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith" J 13
# Output: "Mr%20John%20Smith"



def urlify(s):
    if s is None or len(s) <= 0:
        return s

    new_string = ""
    for c in s:
        if c == " ":
            new_string += "%20"
        else:
            new_string += c

    return new_string


data = [
        {
            "input": ["hello world!"], 
            "output": "hello%20world!",
        },
        {
            "input": ["abc dab cdabcd  "], 
            "output": "abc%20dab%20cdabcd%20%20",
        },
        {
            "input": ["  h ey"], 
            "output": "%20%20h%20ey",
        },
        {
            "input": [" hey"], 
            "output": "%20hey",
        },
        {
            "input": ["1@#  "], 
            "output": "1@#%20%20",
        },
        {
            "input": [" "], 
            "output": "%20",
        },
        {
            "input": ["  "], 
            "output": "%20%20",
        }
    ]


from helper import Test
test = Test()
test.check(urlify, data)
