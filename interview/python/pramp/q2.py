# Word Count Engine
# Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.


# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"

# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"], 
#           ["get", "1"], ["by", "1"], ["just", "1"] 


def wordCountEngine(document):
    document = document.lower()

    new_document = ""
    for c in document:
        if  ord('a') <= ord(c) <= ord('z') or c == " ":
            new_document += c

    words = new_document.split()

    word_count = dict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    val_to_word = dict()

    for word in words:
        if word in word_count:
            if word_count[word] in val_to_word:
                val_to_word[word_count[word]].append(word)
            else:
                val_to_word[word_count[word]] = [word]
            del word_count[word]

    max_val_count = max(val_to_word)

    res = []
    while max_val_count > 0:
        if max_val_count in val_to_word:
            for word in val_to_word[max_val_count]:
                res.append([word, str(max_val_count)])
        max_val_count -= 1

    return res


data = [
    {
        "input": ["Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"],
        "output": [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]],
    },
    {
        "input": ["To be, or not to be, that is the question:"],
        "output": [["to","2"],["be","2"],["or","1"],["not","1"],["that","1"],["is","1"],["the","1"],["question","1"]],
    },
    {
        "input": ["Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "],
        "output": [["and","4"],["every","3"],["is","3"],["a","3"],["quotation","3"],["all","2"],["book","1"],["house","1"],["out","1"],["of","1"],["forests","1"],["mines","1"],["stone","1"],["quarries","1"],["man","1"],["from","1"],["his","1"],["ancestors","1"]],
    },
    {
        "input": ["I have failed over and over and over again in my life and that is why I succeed."],
        "output": [["over","3"],["and","3"],["i","2"],["have","1"],["failed","1"],["again","1"],["in","1"],["my","1"],["life","1"],["that","1"],["is","1"],["why","1"],["succeed","1"]],
    },
    {
        "input": ["Look If you had One shot, Or one opportunity, To seize everything you ever wanted, In one moment, Would you capture it, Or just let it slip?"],
        "output": [["you","3"],["one","3"],["or","2"],["it","2"],["look","1"],["if","1"],["had","1"],["shot","1"],["opportunity","1"],["to","1"],["seize","1"],["everything","1"],["ever","1"],["wanted","1"],["in","1"],["moment","1"],["would","1"],["capture","1"],["just","1"],["let","1"],["slip","1"]],
    },
    {
        "input": ["Cause I'm Slim Shady, yes I'm the real Shady, All you other Slim Shadys are just imitating So won't the real Slim Shady, please stand up, Please stand up, Please stand up"],
        "output": [["slim","3"],["shady","3"],["please","3"],["stand","3"],["up","3"],["im","2"],["the","2"],["real","2"],["cause","1"],["yes","1"],["all","1"],["you","1"],["other","1"],["shadys","1"],["are","1"],["just","1"],["imitating","1"],["so","1"],["wont","1"]],
    },
]


from helper import Test
test = Test()
test.check(wordCountEngine, data)
