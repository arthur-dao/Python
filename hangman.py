import random

def loadWord():
    wordList = ["banana", "apple", "durian", "mango", "carrot"]

    word = random.choice(wordList)
    word = word.upper()

    return word

def startRound(x):
    hiddenWord = "_" * len(loadedWord)
    print("Round Started\n")
    print("Word Length: " + str(len(loadedWord)) + "\n" + hiddenWord)
    print("\n")


    guessed = False
    tries = 5
    guessedLetters = []
    guessedWords = []

    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        
        #checks if the guess is in the alphabet
        if (guess.isalpha() and len(guess) == 1):
            if (guess in guessedLetters):
                print("Letter already guessed:", guess)
                tries -= 1
                print("Tries: ", tries)
            elif (guess not in loadedWord):
                print(guess, "is not in the word")
                tries -= 1
                guessedLetters.append(guess)
                print("Tries: ", tries)
            else:
                print(guess, "is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(hiddenWord)
                indices = [i for i, letter in enumerate(loadedWord) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                hiddenWord = "".join(wordAsList)
                print("Tries: ", tries)

                if ("_" not in hiddenWord):
                    print("Congratulations!")
                    guessed = True
        elif (guess.isalpha()):
            if (guess in guessedWords):
                print("Word already guessed:", guess)
                tries -= 1
                print("Tries: ", tries)
            elif (guess != loadedWord):
                print(guess, "is not the word")
                tries -= 1
                guessedWords.append(guess)
                print("Tries: ", tries)
            else:
                print("Congratulations!")
                guessed = True
                hiddenWord = loadedWord
        else:
            print("Invalid Guess")

        print(hiddenWord)
        print("\n")

loadedWord = loadWord()
startRound(loadedWord)
while (input("Restart Game? (Y/N): ").upper() == "Y"):
    loadedWord = loadWord()
    startRound(loadedWord)