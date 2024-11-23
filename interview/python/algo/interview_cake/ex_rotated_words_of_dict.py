# Write a function for finding the index of the "rotation point,"


# I opened up a dictionary to a page in the middle and started flipping through,
# looking for words I didn't know.
# I put each word I didn't know at increasing indices in a huge list I created in memory.
# When I reached the end of the dictionary,
# I started from the beginning and did the same thing until I reached the page I started at.
#
# Now I have a list of words that are mostly alphabetical,
# except they start somewhere in the middle of the alphabet, reach the end,
# and then start from the beginning of the alphabet. In other words,
# this is an alphabetically ordered list that has been "rotated."
#
# For example:
# words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]


def find_rotation_point(words):
    first_word = words[0]

    low = 0
    high = len(words)

    while low <= high:
        mid = (high+low)//2

        if words[mid] <= first_word:
            high = mid
        else:
            low = mid

        if (low+1) == high:
            return high

    return -1



print (find_rotation_point(['cape', 'cake'])) # 1
print (find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])) # 4

print (find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])) # 5
