# Single Riffle Shuffle
#
# I suspect the online poker game I'm playing shuffles cards by doing a single riffle. ↴
#
# To prove this, let's write a function to tell us
# if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2.
#
# We'll represent a stack of cards as a list of integers in the range 1...52
# (since there are 52 distinct cards in a deck).
# 
# Reference:
# https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation


import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    len_half1 = len(half1)
    len_half2 = len(half2)
    len_deck = len(shuffled_deck)

    if len_deck != (len_half1 + len_half2):
        return False

    i_half1 = 0
    i_half2 = 0
    i_deck = 0

    while i_half1 < len_half1 and i_half2 < len_half2 and i_deck < len_deck:
        if shuffled_deck[i_deck] == half1[i_half1]:
            i_deck += 1
            i_half1 += 1
        elif shuffled_deck[i_deck] == half2[i_half2]:
            i_deck += 1
            i_half2 += 1
        else:
            return False

    while i_half1 < len_half1 and i_deck < len_deck:
        if shuffled_deck[i_deck] != half1[i_half1]:
            return False
        i_deck += 1
        i_half1 += 1

    while i_half2 < len_half2 and i_deck < len_deck:
        if shuffled_deck[i_deck] != half2[i_half2]:
            return False
        i_deck += 1
        i_half2 += 1


    return True

# print (is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))


# Tests
class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
