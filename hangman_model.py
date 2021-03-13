### HANGMAN GAME ###
import random

class Game:
    def __init__(self):
        self.word = ''
        self.wrong_guesses=0

    def getWord(self):
        return self.word
        
    def get_wrong_guesses(self):
        return self.wrong_guesses

    def setWord(self,newword):
        self.word = newword

    def wrong_guesses_increase(self):
        self.wrong_guesses += 1

def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

def textmain(wordsfile):
    words=[]
    for line in open(wordsfile):
        line=line.strip('\n')
        words.append(line)
    game=Game()
    right_word = words[random.randint(0,len(words))]
    right_letters = ''

    for _ in range(len(right_word)):
        right_letters += '_'
    print(f'Welcome! The word has {len(right_letters)} letters. You have 10 guesses. Good luck!')

    while game.get_wrong_guesses() < 10:
        guess_letter = str(input('Guess Letter: '))
        if guess_letter in right_word:
            indexes = charposition(right_word, guess_letter)
            for ind in indexes:
                right_letters=list(right_letters)
                right_letters[ind] = right_word[ind]
                right_letters = ''.join(right_letters)
            if right_word == right_letters:
                break
            else:
                print(f'Correct! Right letters this far: {right_letters}')
        else:
            if game.get_wrong_guesses() < 9:
                print(f'Wrong! :D number of wrong guesses left: {9-game.get_wrong_guesses()}')
            else:
                pass
            game.wrong_guesses_increase()

    if game.get_wrong_guesses() == 10:
        print(f'You lost! The word was {right_word}')
    else:
        print(f'Congratz! You figured out that the word was {right_word}')

textmain('hangman_words.txt')

