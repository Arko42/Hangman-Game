Hangman Game - Flask Implementation
This project implements a Hangman game with a clean, modern UI using HTML/CSS for the frontend and Flask for the backend.
Features

Beautiful, responsive UI design with custom CSS
Visual hangman drawing that progresses with incorrect guesses
Interactive virtual keyboard for letter selection
Game state management using Flask sessions
No JavaScript required - works with standard form submissions
Color-coded feedback for correct and incorrect guesses
Game state persistence between requests

Project Structure------------------------
hangman/
│
├── app.py              # Flask application
├── templates/
│   └── index.html      # Main HTML template
└── static/
    └── styles.css      # CSS styles (optional, included in HTML for this example)
    
Setup Instructions---------------
Ensure you have Python and Flask installed:
pip install flask

Save the files in their respective locations:

app.py in the root directory
index.html in a "templates" folder


Run the application:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000/


How To Play-----------

When the game loads, a random word is selected from the list
Click on letters in the virtual keyboard to make guesses
Correct guesses will reveal the letter in the word
Incorrect guesses will progress the hangman drawing
You win by guessing all letters in the word before running out of attempts
You lose if the hangman drawing is completed (6 incorrect guesses)
Click "New Game" to start a new game at any time

Customization---------------
To add more words to the game, edit the words list in the HangmanGame class in app.py.
The frontend uses a color scheme defined with CSS variables which can be easily modified at the top of the CSS section.

Requirements------------
Python 3.6+
Flask
