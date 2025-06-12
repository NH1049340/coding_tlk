import random
import tkinter as tk
from tkinter import messagebox

words = ["python", "computer", "keyboard", "challenge", "program", "reaction", "internet", "science"]
score = 0
lives = 3
current_word = ""
scrambled_word = ""

def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def new_round():
    global current_word, scrambled_word
    if lives <= 0:
        messagebox.showinfo("Game Over", f"💀 Game Over! Final score: {score}")
        root.destroy()
        return
    current_word = random.choice(words)
    scrambled_word = scramble(current_word)
    word_label.config(text=f"🌀 {scrambled_word}")
    entry.delete(0, tk.END)
    hint_label.config(text="")

def check_guess():
    global score, lives
    guess = entry.get().lower()
    if guess == current_word:
        score += 1
        score_label.config(text=f"Score: {score}")
        result_label.config(text="✅ Correct!", fg="green")
        new_round()
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        result_label.config(text=f"❌ Wrong! The word was '{current_word}'", fg="red")
        new_round()

def give_hint():
    global lives
    if lives > 0:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        hint_label.config(text=f"🧠 Hint: Starts with '{current_word[0]}'")
    else:
        messagebox.showinfo("No lives", "You have no lives left!")

# GUI setup
root = tk.Tk()
root.title("🔤 Word Scramble Game")
root.geometry("400x300")

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

check_button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_guess)
check_button.pack()

hint_button = tk.Button(root, text="Hint (-1 life)", font=("Arial", 12), command=give_hint)
hint_button.pack(pady=5)

hint_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
hint_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
score_label.pack(side="left", padx=20)

lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Arial", 12))
lives_label.pack(side="right", padx=20)

new_round()
root.mainloop()

