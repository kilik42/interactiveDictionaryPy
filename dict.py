import json
import difflib
from difflib import get_close_matches

#help(json.load)

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("did you mean %s instead? Enter Y if yes,  or No if no. " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please Double ckeck it."
        else:
            return "We didn't understand your query"

    else:
        return "The word doesnt exist. Please double check it"

word = input("enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)