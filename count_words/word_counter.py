def count_words(text,n):
    words_box = text.split()
    length = len(words_box)
    output = []
    for i in range(0,length-1):
        for j in range(i+1, length):
            if words_box[i] == words_box[j]:
                output.append(words_box[i])
    print output

count_words("Hi, to day is rainy day in Minneapolis and yesterday was rainy day and day one", 3)
