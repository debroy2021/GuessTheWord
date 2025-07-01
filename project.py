import pandas as pd
import random, os
from pyfiglet import Figlet

def filterByDifficulty(words, difficulty):
    updatedWords = []
    for word in words:
        if (difficulty == "easy" and len(word) < 7):
            updatedWords.append(word)
        elif (difficulty == "medium" and len(word) >= 7 and len(word) < 10):
            updatedWords.append(word)
        elif (difficulty == "hard" and len(word) >= 10 and len(word) < 13):
            updatedWords.append(word)
        elif (difficulty == "hell" and len(word) >= 13 and len(word) < 15):
            updatedWords.append(word)
    return updatedWords

def findUniqueGuessChars(guess):
    uniqueGuessChars = []
    for guessChar in guess:
        uniqueChar = True
        uniqueGuessChars.append("")
        for i in range(len(uniqueGuessChars)):
            if (uniqueGuessChars[i] == guessChar):
                uniqueChar = False
        if (uniqueChar):
            uniqueGuessChars[i] = guessChar
        else:
            uniqueGuessChars.pop(i)
    return uniqueGuessChars

def generateGuessedWord(answer, uniqueGuessChars):
    guessedPassword = []
    for char in answer:
        guessedPassword.append("")

    for i in range(len(answer)):
        incorrectGuess = True
        for uniqueChar in uniqueGuessChars:
            if (answer[i] == uniqueChar):
                guessedPassword[i] = answer[i]
                incorrectGuess = False
        if (incorrectGuess):
            guessedPassword[i] = "_"
    return "".join(guessedPassword)

def main():
    os.system("clear")
    df = pd.read_csv("/Users/debarghyaroy/Desktop/Deb/Coding/Python/CS50P/Final Project/words.csv")
    df.drop(columns=["id", "Part of Speech", "Length"], inplace=True)

    words = df["Word"].tolist()
    frequencies = df["Per Million Words"].tolist()

    updatedWords = []
    for i in range(len(words)):
        if not (frequencies[i] > 1000 and len(words[i]) <= 3):
            updatedWords.append(words[i])
    words = updatedWords

    print("Welcome to\n")
    fig = Figlet()
    fig.setFont(font="ansi_shadow")
    print(fig.renderText("Guess The Word!"))
    print("\nPress Enter to continue: ")
    input()
    exit = False
    while not exit:
        os.system("clear")
        print("Please pick your difficulty (Easy/Medium/Hard/Hell): ", end="")

        difficulty = input().lower()
        while (difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "hell"):
            print("\nPlease enter a valid difficulty (Easy/Medium/Hard/Hell): ", end="")
            difficulty = input().lower()

        filteredWords = filterByDifficulty(words, difficulty)
        uniqueGuessChars = []
        correctWord = random.choice(filteredWords)
        guessedWord = generateGuessedWord(correctWord, "")
        while (guessedWord != correctWord):
            os.system("clear")
            print("Difficulty: " + difficulty.capitalize(), end="\n\n")
            print("Word: " + guessedWord)
            print("Now, enter your guess: ", end="")
            guess = input().lower()
            uniqueGuessChars += findUniqueGuessChars(guess)
            guessedWord = generateGuessedWord(correctWord, uniqueGuessChars)

        os.system("clear")
        print("Difficulty: " + difficulty.capitalize(), end="\n\n")
        print("Word: " + guessedWord, end="\n\n")
        print(fig.renderText("You Won!"))
        print("\nWould you like to play again? (Yes/No): ", end = "")
        playAgain = input().lower()
        while (playAgain != "yes" and playAgain != "no"):
            print("\nPlease enter a valid answer (Yes/No): ", end="")
            playAgain = input().lower()
        exit = True if playAgain == "no" else False

if __name__ == "__main__":
    main()
