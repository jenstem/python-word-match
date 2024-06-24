import random


def pickAnswer():
    fromDictionary = {1 : "word-list.txt"}
    game = fromDictionary[random.randint(1, 1)]
    with open(game, 'r') as readDictionary:
        fileList = readDictionary.read()
    wordList = fileList.split("\n")

    pickWord = wordList[random.randint(0, len(wordList) - 1)]
    return pickWord


def createWordBlanks(word):
    listCharacters = [char for char in word]
    wordBlanks = ["_" for _ in listCharacters]
    return wordBlanks


def createDictionary(word):
    wordIndex = {}

    for index, char in enumerate(word):
        wordIndex[index] = char

    return wordIndex


def checkGuess(guess, wordAnswer):
    wordAnswer = createDictionary(wordAnswer)
    correctSpot = []
    correctLetter = []

    for index, character in enumerate(guess):
        if character in wordAnswer[index]:
            correctSpot.append(character)
        elif character in wordAnswer.values():
            correctLetter.append(character)

    return correctSpot, correctLetter


def updateBlanks(correctSpot, correctLetter, startingBlanks):
    updateBlanks = []
    for index, chars in enumerate(correctLetter):
        if chars in correctSpot:
            updateBlanks.append(chars)
        elif startingBlanks[index] != "_":
            updateBlanks.append(startingBlanks[index])
        else:
            updateBlanks.append("_")
    return updateBlanks


def wrongSpot(correctLetter):
    if correctLetter:
        print("You have guessed the correct letter, but in the wrong spot.")
        for letter in correctLetter:
            print(f"{letter}, ", end="")
        print()


def correctGuess(guess, answer):
    return guess == answer


if __name__ == "__main__":
    pickWord = pickAnswer()
    finalBlanks = createWordBlanks(pickWord)
    guesses = []
    flag = True

    while (flag):
        usersGuess = input("\n Guess a five (5) letter word:")
        if (len(usersGuess) != 5):
            print("Please enter a five (5) letter word.")
            continue

        correctSpot, correctLetter = checkGuess(usersGuess, pickWord)
        currentBlanks = updateBlanks(correctSpot, pickWord, finalBlanks)
        print(currentBlanks)

        wrongSpot(correctLetter)

        if correctGuess(usersGuess, pickWord):
            print("Congratulations! You won!")
            flag = False

        finalBlanks = currentBlanks