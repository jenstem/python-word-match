import random


def pickAnswer():
    fromDictionary = {1 : "word-list.py"}
    game = fromDictionary[random.randint(0, 486)]
    with open(game, 'r') as readDictionary:
        fileList = readDictionary.read()
    wordList = fileList.split("\n")

    pickWord = wordList[random.randint(0, len(wordList) - 1)]
    return pickWord


def createWordBlanks(word):
    listCharacters = [char for char in word]
    wordBlanks = ["_" for _ in listCharacters]
    return wordBlanks


def createDictionary (word):
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