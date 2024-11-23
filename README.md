
# Quiz Game

This is a simple Python-based Quiz Game built with Tkinter for the graphical user interface and CSV for loading questions. The game presents a series of questions to the player, who enters answers to receive feedback on correctness, and then a final score at the end.

## Features

- Randomized questions loaded from a CSV file (`questions.csv`).
- User-friendly interface with Tkinter.
- Feedback on correct and incorrect answers.
- Final score display at the end of the game.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `questions.csv` file with the following format:
  ```csv
  question,answer
  What is the capital of France?,Paris
  ```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harishkadhir/quiz_game.git
   cd quiz-game
   ```

2. **Add questions file:**
   - Create a `questions.csv` file in the project directory.
   - Add questions and answers in the format specified above.

3. **Run the game:**
   ```bash
   python quiz_game.py
   ```

## Usage

1. When the game starts, a random question will be displayed.
2. Enter your answer in the input box and press `Submit`.
3. You’ll receive feedback, and the next question will appear.
4. When all questions are completed, you’ll see your final score.

## Code Overview

- **`QuizGame` class:** Manages the main game logic.
- **`load_questions` method:** Reads questions from the `questions.csv` file.
- **`check_answer` method:** Checks if the player's answer is correct and provides feedback.
- **`next_question` method:** Moves to the next question.
- **`end_game` method:** Displays the final score and ends the game.



