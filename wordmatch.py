import random


def pickAnswer():
    fromDictionary = {1 : "word-list.py"}
    game = fromDictionary[random.randint(0, 486)]
    with open(game, 'r') as readDictionary:
        fileList = readDictionary.read()
    wordList = fileList.split("\n")

    pickWord = wordList[random.randint(0, len(wordList) - 1)]
    return pickWord