import pandas as pd
import random
import time
import os


def checker():
	df = pd.read_excel('Word.xlsx')
	wordlist = df.values.tolist()
	#print(wordlist)
	theWord = random.choice(wordlist) #chooses the random word
	fin_Word = "['']".join(theWord) #clean the word
	#print(fin_Word)
	
	atm = 6
	while atm > 0:
		wordcheck = ""
		attempt = str(input("Guess the word: ").upper())
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
					wordcheck = wordcheck + " " + word + " "
				elif word in fin_Word:
					wordcheck = wordcheck + " + "
				else:
					wordcheck = wordcheck + " x "
			print (wordcheck)
			if atm == 0:
				print("Game Over and the word is :", fin_Word)
		
print("""	hi, this is my version of a game Wordle made with python.
	The list of words selected in random are in the excel file.
	Just like the game you have will 6 chances. 
	In each attempt, you will be shown 
	a + symbol if you have a correct letter but in the wrong position,
	a x symbol if you are just wrong with the letter,
	and the Letter for that position if that's correct.

	May the odds be in your favor.
	War. War never changes.
	Toss a coin to your Witcher.
	I don't know. Hakuna Matata. Good Luck!
	""")

checker()