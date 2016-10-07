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
