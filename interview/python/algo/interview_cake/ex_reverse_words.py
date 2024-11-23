# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
#
# stock_prices, where:
# When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.
#
# Example,
# message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
# reverse_words(message)
#
# # Prints: 'steal pound cake'
# print ''.join(message)
#
# Reference:
# https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation


import unittest


def flip_chars(message, start, end):
    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1
    return

def reverse_words(message):

    # reverse full string
    flip_chars(message, 0, len(message)-1)

    # initialize start at 0
    start = 0
    # iterate through the string (i)
    for i in range(len(message)):
        if message[i].isspace():
            end = i-1
            flip_chars(message, start, end)
            start = i + 1

    flip_chars(message, start, len(message)-1)

    return



# Test

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
