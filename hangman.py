# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if (i not in lettersGuessed): return False
    return True;



def getGuessedWord(secretWord, lettersGuessed):
    blank = []
    for i in secretWord: blank.append('_')
    for letter in lettersGuessed:
        for l in range(len(secretWord)):
            if (secretWord[l] == letter): blank[l] = letter
    return "".join(blank)


def getAvailableLetters(lettersGuessed):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for l in alpha:
        if (l not in lettersGuessed): result += l
    return result;
   

def hangman(secretWord):
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    print('-------------')
    usedLetters = []
    guesses = 8
    
    # some additional functions
    def quit():
        print(f'You quit? Ok, the word was {secretWord}!')
    def getHint():
        randomPick = random.choice(secretWord)
        while (randomPick in usedLetters):
            randomPick = random.choice(secretWord)
        print(f'💡Hint: {randomPick} is in the answer!')
        
    while (guesses > 0 and not isWordGuessed(secretWord, usedLetters)):
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {getAvailableLetters(usedLetters)}')
        guess = input('Please guess a letter: ')
            
        if (guess.lower() == 'quit'): 
            quit()
            break
        
        elif (guess.lower() == 'hint'):
            getHint()
            
        elif (guess == '' or guess not in getAvailableLetters(usedLetters) or len(guess) > 1):
            print('Sorry! That is invalid, please enter something valid!')
            print("\n")
            
        elif (guess in usedLetters):
            usedLetters.append(guess)
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, usedLetters)}")
            
            
        elif (guess not in secretWord):
            usedLetters.append(guess)
            guesses -= 1
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, usedLetters)}")
            
        
                
        elif (guess in secretWord): 
            usedLetters.append(guess)
            print(f'Good guess: {getGuessedWord(secretWord, usedLetters)}')
            

            
        print("")
        print('-------------')
        print("")
        
    if (isWordGuessed(secretWord, usedLetters)): print('Congratulations, you won!')
    elif (not isWordGuessed(secretWord, usedLetters) and guess.lower() != 'quit'): print(f'Sorry, you ran out of guesses. The word was {secretWord}.')
    
    print('Good Game! 🤜🏼🤛🏼')





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)