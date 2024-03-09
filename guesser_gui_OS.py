import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def check_guess(event=None):
    global attempts, secret_number, entry, result_label, high_score

    try:
        guess = int(entry.get())
        entry.delete(0, tk.END)
        attempts += 1

        if guess < secret_number:
            result_label.config(text="Too low. Try again!")
        elif guess > secret_number:
            result_label.config(text="Too high. Try again!")
        else:
            result_label.config(text=f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            if attempts < high_score:
                high_score = attempts
            messagebox.showinfo("Congratulations!", f"You guessed the number {secret_number} in {attempts} attempts."
                                                     f"\n\nYour High Score: {high_score}")
            play_again_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
            root.bind("<Return>", restart_game)
            root.unbind("<Return>", check_guess)

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")


def restart_game(event=None):
    global secret_number, attempts, entry, result_label, play_again_button

    play_again_button.grid_forget()
    attempts = 0
    secret_number = random.randint(1, 100)
    result_label.config(text="")
    entry.delete(0, tk.END)

    root.bind("<Return>", check_guess)
    root.unbind("<Return>", restart_game)
    play_again_button.grid_forget()


def guess_the_number():
    global secret_number, attempts, entry, result_label, high_score, root, play_again_button

    secret_number = random.randint(1, 100)
    attempts = 0
    high_score = float('inf')  # Initialize high score to positive infinity

    root = tk.Tk()
    root.title("Guess the Number")

    content_frame = ttk.Frame(root, padding="10")
    content_frame.grid(row=0, column=0, padx=10, pady=10)

    welcome_label = ttk.Label(content_frame, text="Welcome to Guess the Number!", font=("Arial", 14, "bold"))
    welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

    info_label = ttk.Label(content_frame, text="I'm thinking of a number between 1 and 100.")
    info_label.grid(row=1, column=0, columnspan=2, pady=10)

    entry = ttk.Entry(content_frame, width=10)
    entry.grid(row=2, column=0, padx=5, pady=10)

    entry.bind("<Return>", check_guess)

    check_button = ttk.Button(content_frame, text="Check", command=check_guess)
    check_button.grid(row=2, column=1, padx=5, pady=10)

    result_label = ttk.Label(content_frame, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    play_again_button = ttk.Button(content_frame, text="Play Again", command=restart_game)
    play_again_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
    play_again_button.grid_forget()

    root.mainloop()

if __name__ == "__main__":
    guess_the_number()
