import pandas as pd
import random



def checker():
	df = pd.read_excel('Word.xlsx')
	wordlist = df.values.tolist()
	#print(wordlist)
	theWord = random.choice(wordlist) #chooses the random word
	fin_Word = "['']".join(theWord) #clean the word
	#print(fin_Word)
	atm = 6
	while atm > 0:
		attempt = str(input("Guess the word: "))
		if (len(attempt) != 5):
			atm -= 1
			print("only five letters allowed \n Remaining Attempts :", atm)
		elif attempt == fin_Word:
			print("You Win!")
			break
		else:
			atm -= 1
			print("Not quite right \n Remaining Attempts :", atm)
			for char, word in zip(fin_Word,attempt):
				if word in fin_Word and word in char:
					print(word + " is in the right place")
				elif word in fin_Word:
					print(word + " is not in the right place ")
				else:
					print("✗ this is just wrong")
			if atm == 0:
				print("Game Over and the word is :", fin_Word)
		
checker()