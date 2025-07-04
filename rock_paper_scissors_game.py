import tkinter as tk
import random

#Colors and Styles
BG_COLOR = "#1e1e2f"
BTN_COLOR = "#ff914d"
TEXT_COLOR = "#f0f0f0"
PANEL_COLOR = "#2e2e42"
FONT_MAIN = ("Helvetica", 14)
FONT_HEADING = ("Helvetica", 18, "bold")

#Window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("420x450")
window.configure(bg=BG_COLOR)

# Scores
user_score = 0
computer_score = 0

#Functions
def play(choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    user_choice_label.config(text=f"You chose: {choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "YOU WIN!! 🎉"
        user_score += 1
    else:
        result = "You Lose! 😞"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You - {user_score} | Computer - {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose:")
    computer_choice_label.config(text="Computer chose:")
    result_label.config(text="Result")
    score_label.config(text="Score: You - 0 | Computer - 0")

def quit_game():
    window.destroy()

#Widgets
heading = tk.Label(window, text="Rock Paper Scissors", font=FONT_HEADING, bg=BG_COLOR, fg=TEXT_COLOR)
heading.pack(pady=15)

# Buttons
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

style_button = lambda text, cmd: tk.Button(button_frame, text=text, width=10, bg=BTN_COLOR, fg="black",
font=FONT_MAIN, relief="flat", command=cmd)

rock_button = style_button("Rock", lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = style_button("Paper", lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = style_button("Scissors", lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Labels
user_choice_label = tk.Label(window, text="You chose:", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="Computer chose:", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
computer_choice_label.pack(pady=5)

result_label = tk.Label(window, text="Result", font=("Helvetica", 16, "bold"), bg=BG_COLOR, fg="#ffd369")
result_label.pack(pady=15)

score_label = tk.Label(window, text="Score: You - 0 | Computer - 0", font=FONT_MAIN, bg=PANEL_COLOR, fg=TEXT_COLOR, pady=10, padx=10)
score_label.pack(pady=10)

# Control Buttons
control_frame = tk.Frame(window, bg=BG_COLOR)
control_frame.pack(pady=20)

reset_button = tk.Button(control_frame, text="Play Again", width=12, bg="#5ccfe6", fg="black", font=FONT_MAIN,
command=reset_game)
reset_button.grid(row=0, column=0, padx=10)

quit_button = tk.Button(control_frame, text="Quit", width=12, bg="#ef476f", fg="white", font=FONT_MAIN,
command=quit_game)
quit_button.grid(row=0, column=1, padx=10)

window.mainloop()     
