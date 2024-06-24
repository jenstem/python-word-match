from flask import Flask, jsonify

from wordmatch import pickAnswer, createWordBlanks
app = Flask(__name__)

@app.route('/startGame', methods=['GET'])
def startGame():
    pickWord = pickAnswer()
    blanks = createWordBlanks(pickWord)
    return jsonify(blanks)