import tkinter as tk
from tkinter import messagebox
import csv
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")

        self.current_question_index = 0
        self.correct_answers = 0
        self.total_questions = 0
        self.questions = self.load_questions()
        if not self.questions:
            messagebox.showerror("Error", "No questions available. Please check your questions.csv file.")
            master.quit()
            return
        random.shuffle(self.questions)  # Shuffle questions to randomize

        self.question_label = tk.Label(master, text=self.questions[self.current_question_index][0], font=('Helvetica', 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=('Helvetica', 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer, font=('Helvetica', 14))
        self.submit_button.pack(pady=10)
        self.submit_button.bind("<Enter>", self.on_button_enter)
        self.submit_button.bind("<Leave>", self.on_button_leave)

        self.end_button = tk.Button(master, text="End Game", command=self.end_game, font=('Helvetica', 14))
        self.end_button.pack(pady=10)
        self.end_button.bind("<Enter>", self.on_button_enter)
        self.end_button.bind("<Leave>", self.on_button_leave)

        self.feedback_label = tk.Label(master, text="", font=('Helvetica', 12))
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(master, text="", font=('Helvetica', 14))  # Initially empty
        self.score_label.pack(pady=10)

    def load_questions(self):
        questions = []
        try:
            with open('questions.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) == 2:  # Ensure valid format (question, answer)
                        questions.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "questions.csv file not found.")
        return questions

    def check_answer(self):
        answer = self.answer_entry.get()
        correct_answer = self.questions[self.current_question_index][1]
        if answer.lower() == correct_answer.lower():
            self.correct_answers += 1
            self.feedback_label.config(text="Correct answer!", fg="green")
        else:
            self.feedback_label.config(text=f"Wrong answer! The correct answer is: {correct_answer}", fg="red")

        self.total_questions += 1
        self.answer_entry.delete(0, tk.END)  # Clear the answer box

        # Show feedback and then move to next question after 3 seconds
        self.master.after(3000, self.next_question)  # 3000 milliseconds = 3 seconds

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.question_label.config(text=self.questions[self.current_question_index][0])
            self.feedback_label.config(text="")
        else:
            self.end_game()  # Call end_game to handle the end of the quiz

    def end_game(self):
        self.question_label.config(text="Game Over!")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.end_button.pack_forget()
        final_score = self.correct_answers / self.total_questions * 100 if self.total_questions > 0 else 0
        self.score_label.config(text=f"Final Score: {final_score:.2f}%")
        self.feedback_label.config(text="")

    def on_button_enter(self, event):
        event.widget.config(bg="lightgreen")  # Change the background color to green on hover

    def on_button_leave(self, event):
        event.widget.config(bg="SystemButtonFace")  # Reset to the default color

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()
