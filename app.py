from flask import Flask, jsonify

from wordmatch import pickAnswer, createWordBlanks
app = Flask(__name__)

@app.route('/startGame', methods=['GET'])
def startGame():
    """
    Initiates the game by selecting a word and creating corresponding blanks.

    Returns:
        jsonify:  A JSON response containing the word blanks for the selected word.
    """
    pickWord = pickAnswer()
    blanks = createWordBlanks(pickWord)
    return jsonify(blanks)
