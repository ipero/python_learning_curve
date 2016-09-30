import urllib

def read_text():
    quotes = open ("/Users/Artizan-mac/Prime Academy/Learning curve/python/profanity_editor/movie_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    connection.close()
    if "true" in output:
        print ("Profanity found!!! Please correct it!")
    elif "false" in output:
        print("You're good, no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()

