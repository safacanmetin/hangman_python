from words import words
import random
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #unique letters in the word - with set method
    alphabet = set(string.ascii_letters)
    usedLetters = set()
    
    lives = 7
    
    #getting input
    while len(wordLetters) > 0 and lives > 0: 
        #letters used
        print("You have", lives,"lives left and you have used these letters: ", "".join(usedLetters))
        
        #what current word is 
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " ".join(wordList))
        
        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                
            else:
                lives -=1 # 1 life is gone
                print("Letter is not in the word.")

        elif userLetter in userLetter:
            print("You already used that character. Try another one.")

        else:
            print("Invalid character. Try a valid one.")
        
    if lives == 0:
        print("No lives left. Game over. The word was ", word)
    print("You guessed the word ", word, "!!!")
                
hangman()    
