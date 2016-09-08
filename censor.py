text = ''
word = ''

def censor(text,word):
	word.split()
	if word in text:
		wordlen = int()
		wordlen = len(word)

		asterix = wordlen * '*'	

		newword = text.replace(word,asterix)
		return newword

print censor("this hack is wack hack", "hack") 