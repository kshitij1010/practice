class Trie:
    def __init__(self):
        self.subdict = {}
        self.end = False

# using Trie class
class Autocomplete:
    def __init__(self):
        self.head = Trie()

    def insert(self, username):
        curr = self.head
        for c in username:
            if c not in curr.subdict:
                curr.subdict[c] = Trie()
            curr = curr.subdict[c]

        curr.end = True
        return

    def get_words(self, node, prefix, words):
        if node is None:
            return

        if node.end:
            words.append(prefix)

        for key, value in node.subdict.items():
            self.get_words(value, prefix + key, words)
        return

    def search(self, prefix):
        curr = self.head
        for c in prefix:
            if c not in curr.subdict:
                return []
            curr = curr.subdict[c]
        words = []
        self.get_words(curr, prefix, words)
        return words


# without using Trie class
class Autocomplete2:
    def __init__(self):
        self.head = {}

    def insert(self, username):
        curr = self.head
        for c in username:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr["*"] = True
        return

    def get_words(self, node, prefix, words):
        if len(node) == 0 or node is None:
            return

        if node.get("*"):
            words.append(prefix)

        for key, value in node.items():
            if key == '*':
                continue
            self.get_words(node[key], prefix + key, words)
        return

    def search(self, prefix):
        curr = self.head
        for c in prefix:
            if c not in curr:
                return []
            curr = curr[c]
        words = []
        self.get_words(curr, prefix, words)
        return words

auto = Autocomplete2()
auto.insert("ab")
auto.insert("abc")
auto.insert("abde")
auto.insert("abcd")
auto.insert("def")
auto.insert("defz")
auto.insert("")


print (auto.search("a"))
print (auto.search("abc"))
print (auto.search("def"))
print (auto.search(""))
print (auto.search("qwert"))
