# BoggleBoard
# Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
# Find all possible words that can be formed by a sequence of adjacent characters.
# Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
# https://leetcode.com/problems/word-search-ii/
# Reference:
# https://www.geeksforgeeks.org/boggle-set-2-using-trie/


class Trie:
    def __init__(self):
        self.dictionary = dict()
        self.end = False


class BoggleBoard:
    def __init__(self, dictionary):
        self.head = Trie()
        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        cur = self.head

        for c in word:
            if c not in cur.dictionary:
                cur.dictionary[c] = Trie()
            cur = cur.dictionary[c]

        cur.end = True
        return

    def boggle_search(self, boggle):
        if boggle is None or len(boggle) == 0 or len(boggle[0]) == 0:
            return []

        res = set()
        cur = self.head
        for i in range(len(boggle)):
            for j in range(len(boggle[0])):
                self.search_word(cur, boggle, boggle[i][j], res, i, j)

        return res

    def search_word(self, cur_node, boggle, word, res, row, col):
        if row < 0 or row >= len(boggle) or col < 0 or col >= len(boggle[0]):
            return

        c = boggle[row][col]
        if c not in cur_node.dictionary:
            return

        cur_node = cur_node.dictionary[c]
        if cur_node.end:
            res.add(word)

        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < len(boggle) and j >= 0 and j < len(boggle[0]):
                    self.search_word(cur_node, boggle, word+boggle[i][j], res, i, j)

        return


dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]
d = BoggleBoard(dictionary)

boggle = [
            ['G','I','Z'],
            ['U','E','K'],
            ['Q','S','E'],
         ]

print (d.boggle_search(boggle))
