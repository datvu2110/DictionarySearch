import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0:
		temp = get_close_matches(word,data.keys())[0]
		print(temp)
		yesno = input ("Did you mean %s instead? Enter Y if yes, or N if no. " % temp)
		if yesno == "Y" or yesno == "y":
			return data[temp]
		elif yesno == "N" or yesno =="n":
			return "The word does not exist. Please check it again"
		else:
			return "Please search again"
	else:
		return "The word does not exist. Please double check"

word = input("Enter word: ")

res = translate(word)
if type(res)== list:
	for each in res:
		print(each)
else:
	print(res)