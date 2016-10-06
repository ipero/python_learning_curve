from operator import itemgetter
def count_words(text,n):
    words_box = text.split()
    output = []

    while(len(words_box)>0):
        word = words_box[0]
        words_box.remove(words_box[0])
        instance = 1
        if(len(words_box)>=1):
            i = 0
            while(i<len(words_box)):
                if(word==words_box[i]):
                    instance = instance + 1
                    words_box.remove(words_box[i])
                i = i + 1
        output.append((word, instance))
    output = sorted(output, key=itemgetter(0))
    output = sorted(output, key=itemgetter(1), reverse=True)
    print output


count_words("hi, a to day is rainy day in minneapolis and yesterday was rainy day and day one one one", 3)
