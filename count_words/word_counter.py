# Implement a function count_words() in Python that takes as input a string TEXT
# and a number N, and returns the n most frequently-occuring words in s.
# The return value should be a list of tuples - the top n words paired with their
# respective counts [(<word>, <count>), (<word>, <count>), ...], sorted
# in descending count order.
#
# You can assume that all input will be in lowercase and that there will be no
# punctuations or other characters (only letters and single separating spaces).
# In case of a tie (equal count), order the tied words alphabetically.
#
# E.g.:
#
# print count_words("betty bought a bit of butter but the butter was bitter",3)
# Output:
#
# [('butter', 2), ('a', 1), ('betty', 1)]
from operator import itemgetter
def count_words(text,n):
    words_box = text.split()
    output = []

    while(len(words_box)>0):
        word = words_box[0]
        instance = words_box.count(word)
        words_box = filter(lambda x: x != word, words_box)
        output.append((word, instance))

    output = sorted(output, key=itemgetter(0))
    output = sorted(output, key=itemgetter(1), reverse=True)[:n]

    print output

count_words("a bb bb ccc ccc ccc dddd dddd dddd dddd"
    " betty bought a bit of butter but the butter was bitter"
    " today was a rainy day and day one one one", 3)
