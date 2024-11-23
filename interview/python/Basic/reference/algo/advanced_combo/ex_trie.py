# Example of Trie
#
# Define add word in Trie
# Also, define the method to search the word in the trie
#
# Reference:
# https://www.youtube.com/watch?v=o6563NNbdtg&feature=youtu.be

class Trie():
    def __init__(self):
        self.head = {}

    def add_word(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        # since we added a word in the Trie, to indicate that this is the end of the word we add key "*" with value True
        curr["*"] = True
        return

    def search_word(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                # since char is not in Trie, it does not belong in Trie so return False
                return False
            else:
                curr = curr[ch]
        # now, we have gone thorugh all char of words and all chars are in Trie
        # so we confirm if that is complete word by checking the status of "*"

        if "*" in curr:
            return True
        return False


d = Trie() # d for dictionary
d.add_word("abcd")
d.add_word("hey")
d.add_word("hi")
d.add_word("hello")

print ("Word \"abcd\" in dictionary? =>", d.search_word("abcd"))
print ("Word \"a\" in dictionary? =>", d.search_word("a"))
print ("Word \"heyy\" in dictionary? =>", d.search_word("heyy"))
print ("Word \"hey\" in dictionary? =>", d.search_word("hey"))
print ("Word \"hello\" in dictionary? =>", d.search_word("hello"))
print ("Word \"hiw\" in dictionary? =>", d.search_word("hiw"))
print ("Word \"hi\" in dictionary? =>", d.search_word("hi"))
print ("Word \" \" in dictionary? =>", d.search_word(" "))
print ("Word \"\" in dictionary? =>", d.search_word(""))

d.add_word("")
d.add_word(" ")
print ("After adding \"\" and \" \" (empty char as a word and space as a word)")
print ("Word \" \" in dictionary? =>", d.search_word(" "))
print ("Word \"\" in dictionary? =>", d.search_word(""))
