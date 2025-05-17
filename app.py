from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# -------------------------
# Hangman Game Class
# -------------------------
class HangmanGame:
    def __init__(self):
        self.words = [
            "python", "programming", "computer", "algorithm", "development",
            "keyboard", "function", "language", "variable", "javascript",
            "database", "network", "software", "hardware", "interface",
            "terminal", "iteration", "structure", "application", "framework",
            "repository", "version", "control", "debugging", "scripting",
            "compiler", "interpreter", "syntax", "runtime", "exception",
            "object", "class", "method", "property", "inheritance",
            "encapsulation", "polymorphism", "abstraction", "module",
            "package", "library", "dependency", "installation", "configuration",
            "environment", "deployment", "testing", "debug", "refactor",
            "optimization", "performance", "scalability", "security",
            "protocol", "API", "endpoint", "request", "response",
            "header", "body", "status", "code", "client", "server",
            "database", "query", "transaction", "connection", "schema",
            "table", "row", "column", "index", "key", "constraint",]
        self.max_attempts = 6

    def get_new_word(self):
        return random.choice(self.words)

# -------------------------
# Routes
# -------------------------

@app.route('/')
def index():
    if 'word' not in session:
        return redirect(url_for('new_game'))

    word = session['word']
    guessed_letters = session.get('guessed_letters', [])
    attempts_left = session.get('attempts_left', 6)
    game_over = session.get('game_over', False)
    won = session.get('won', False)

    # Word display
    display_word = [letter if letter in guessed_letters else '' for letter in word]

    # Letter status
    correct_letters = [letter for letter in guessed_letters if letter in word]
    incorrect_letters = [letter for letter in guessed_letters if letter not in word]

    # Win check
    if not game_over and all(letter in guessed_letters for letter in word):
        won = True
        game_over = True
        session['won'] = True
        session['game_over'] = True

    return render_template('index.html',
                           display_word=display_word,
                           word=word,
                           guessed_letters=guessed_letters,
                           correct_letters=correct_letters,
                           incorrect_letters=incorrect_letters,
                           attempts_left=attempts_left,
                           max_attempts=6,
                           game_over=game_over,
                           won=won,
                           hangman_state=6 - attempts_left)

@app.route('/guess', methods=['POST'])
def guess():
    if session.get('game_over', False):
        return redirect(url_for('index'))

    letter = request.form.get('letter', '').lower()

    if letter.isalpha() and len(letter) == 1:
        guessed_letters = session.get('guessed_letters', [])
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            session['guessed_letters'] = guessed_letters

            if letter not in session['word']:
                session['attempts_left'] = session.get('attempts_left', 6) - 1
                if session['attempts_left'] <= 0:
                    session['game_over'] = True

    return redirect(url_for('index'))

@app.route('/new-game', methods=['GET', 'POST'])
def new_game():
    game = HangmanGame()
    session.clear()
    session['word'] = game.get_new_word()
    session['guessed_letters'] = []
    session['attempts_left'] = game.max_attempts
    session['game_over'] = False
    session['won'] = False
    return redirect(url_for('index'))

# -------------------------
# Custom Template Filter
# -------------------------
@app.template_filter('in_list')
def in_list(item, list_):
    return item in list_

# -------------------------
# Run App
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
