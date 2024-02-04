# SelvaRagul_Hangman_and_Quiz
Here's a concise description for your Hangman and Quiz project using Tkinter in Python:

**Hangman & Quiz Game GUI Application**

A simple GUI-based application developed in Python using the Tkinter module. The user can choose between two classic games: Hangman or Quiz. The homepage presents three options - Hangman, Quiz, or Quit.

- **Hangman Game:**
  - User guesses letters to unveil a hidden word.
  - Limited to five chances. Exceeding chances results in game over.
  - Clicking Quit option returns to the homepage.
- **Quiz Game:**
  - User faces four random questions out of a pool of 25.
  - Results displayed in a messagebox at the end of the questions.
  - Clicking Quit option returns to the homepage.
- **Quit Option:**
  - Ends the game and closes the application.

**Modules Used:**
- `Button`
- `Frame`
- `Label`
- `Text`
- `Grid`
- `MessageBox` functions (`ShowInfo`, `ShowWarning`, `ShowError`, `AskQuestion`, `AskYesNo`, `AskRetryCancel`)
- `Date` and `Time` modules
- `Random` module for question randomization

**Note:** 
- Utilizes Tkinter for a user-friendly interface.
- Provides an engaging experience with classic games.
- Allows repeated gameplay until the user chooses to quit.
