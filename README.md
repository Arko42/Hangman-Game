Hangman GameWelcome to the Hangman Game! This is a classic word-guessing game built with Flask, Python, HTML, and CSS. Guess the hidden word letter by letter before you run out of attempts and the hangman is complete!

🎮 Game OverviewThe objective of Hangman is to guess a word chosen by the computer. You are given a certain number of attempts (in this game, 6 attempts). For each incorrect letter you guess, a part of the hangman figure is drawn. If the hangman figure is completed before you guess the word, you lose. If you guess all the letters in the word, you win!Features:Interactive Gameplay: Guess letters using an on-screen keyboard.Visual Feedback: The hangman drawing progresses with each incorrect guess.Attempt Tracker: Clearly displays the number of attempts remaining.Guessed Letters: Shows which letters you've already tried, categorized as correct or incorrect.Responsive Design: Playable on various screen sizes (desktop, tablet, mobile).New Game Option: Easily start a new game at any time.

📁 Project StructureThe project is organized into the following main files:
├── app.py
├── index.html
├── requirements.txt
└── README.md

app.py: This is the core Python Flask application file. It handles all the game logic, including word selection, managing game state (guessed letters, attempts left, win/loss conditions), and routing HTTP requests.index.html: This file contains the HTML structure and CSS styling for the game's user interface. It defines how the game looks, including the hangman drawing, word display, keyboard, and status messages.requirements.txt: This file lists all the Python dependencies required to run the Flask application. It's used to set up the correct environment.README.md: This file (the one you're reading!) provides an overview of the project, game instructions, setup guide, and file structure.

🚀 How to Run the Game
To get the Hangman game up and running on your local machine, 

follow these simple steps:
PrerequisitesMake sure you have Python 3.x installed on your system.
InstallationClone the repository (if applicable) : git clone <repository_url>
cd hangman-game
(If you downloaded the files directly,
navigate to the project directory.)
Create a virtual environment (recommended):python -m venv venv
Activate the virtual environment:On Windows:.\venv\Scripts\activate
On macOS/Linux:source venv/bin/activate
Install the required Python packages:pip install -r requirements.txt
Running the ApplicationSet the Flask application:export FLASK_APP=app.py  # For macOS/Linux
set FLASK_APP=app.py     

# For Windows
Run the Flask development server:flask run
Access the game:Open your web browser and go to http://127.0.0.1:5000/ (or the address shown in your terminal).

🛠️ Technologies Used
Python: The primary programming language for the backend logic.
Flask: A lightweight web framework for Python.
HTML: For structuring the web page content.
CSS: For styling the game's appearance and ensuring responsiveness.

🤝 ContributingIf you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

📄 LicenseThis project is open source and available under the MIT License (if you have one, otherwise remove this section).

Enjoy playing Hangman!
