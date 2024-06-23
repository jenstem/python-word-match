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