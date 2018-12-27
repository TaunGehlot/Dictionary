import difflib
import json
def translate(word):
    word=word.lower()
    if word.capitalize() in dic:
        return dic[word.capitalize()]
    elif word in dic:
        return dic[word]
    elif difflib.get_close_matches(word, dic.keys(), n=3, cutoff=0.8):
        most=difflib.get_close_matches(word, dic.keys(), n=3, cutoff=0.8)
        print("Did you mean ",most[0],"?")
        choice=input("Press Y if YES: ")
        if choice=='Y' or choice=='y':
            return dic[most[0]]
        else:
            return "We did not understand the word."
    else:
        return "This word does not exist in the memory."


dic=json.load(open("076 data.json"))
ch='Y'
while ch=='Y' or ch=='y':
    word=input("Enter word: ")
    meaning=translate(word)
    if type(meaning)==list:
        for meanings in meaning:
            print(meanings)
    else:
        print(meaning)
    ch=input("Do yo wish to continue?(Y/N) : ")
