import random


def pickAnswer():
    """
    Selects a random word from a specified dictionary file.

    Returns:
        str: A randomly selected word from the word list.
    """
    fromDictionary = {1 : "word-list.txt"}
    game = fromDictionary[random.randint(1, 1)]
    with open(game, 'r') as readDictionary:
        fileList = readDictionary.read()
    wordList = fileList.split("\n")

    pickWord = wordList[random.randint(0, len(wordList) - 1)]
    return pickWord


def createWordBlanks(word):
    """
    Generates a list of underscores representing the letters in the given word.

    Args:
        word (str): The word for which blanks are to be created.

    Returns:
        list: A list of underscores representing each character in the word.
    """
    listCharacters = [char for char in word]
    wordBlanks = ["_" for _ in listCharacters]
    return wordBlanks


def createDictionary(word):
    """
    Creates a dictionary mapping the index of each character in the word to the character.

    Args:
        word (str): The word to be indexed.

    Returns:
        dict: A dictionary with indices as keys and characters as values.
    """
    wordIndex = {}

    for index, char in enumerate(word):
        wordIndex[index] = char

    return wordIndex


def checkGuess(guess, wordAnswer):
    """
    Compares the user's guess with the answer word and identifies correct letters and their positions.

    Args:
        guess (str): The user's guessed word.
        wordAnswer (str): The correct answer word.

    Returns:
        tuple: A tuple containing two lists - correctSpot and correctLetter.
    """
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
    """
    Updates the list of blanks based on correct letters guessed by the user.

    Args:
        correctSpot (list): List of letters guessed correctly in the correct position.
        correctLetter (list): List of letters guessed correctly but in the wrong position.
        startingBlanks (list): The current state of the blanks.

    Returns:
        list: An updated list of blanks reflecting the correct guesses.
    """
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
    """
    Notifies the user of letters that were guessed correctly but are in the wrong position.

    Args:
        correctLetter (list): List of letters that were guessed correctly but in the wrong position.
    """
    if correctLetter:
        print("You have guessed the correct letter, but in the wrong spot.")
        for letter in correctLetter:
            print(f"{letter}, ", end="")
        print()


def correctGuess(guess, answer):
    """
    Checks if the user's guess matches the answer.

    Args:
        guess (str): The user's guessed word.
        answer (str): The correct answer word.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
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
