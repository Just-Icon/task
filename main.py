# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from ast import Num
from cgitb import text


def read_file_content(filename):
    # [assignment] Add your code here 
    file_path = "C:/Users/ISRAEL/Desktop/Reading-Text-Files/story.txt"
    with open(file_path) as f:
        text = print(f.read())
    return text
    
read_file_content("./story.txt")


def count_words(read_file_content):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    myText = text.split(" ")
    myDict = {}
    
    for word in myText:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

count_words(read_file_content)

    #return {"as": 10, "would": 20}'''