import tkinter as tk
from tkinter import font

# Window
window = tk.Tk()
window.title("calculator")
window.geometry("600x650")
window.configure(bg="#1e1e1e")

# Frames
root_frame = tk.Frame(window, bg="#1e1e1e")
root_frame.pack()

display_frame = tk.LabelFrame(root_frame, width=400, height=80, bg="#1e1e1e")
display_frame.grid(row=0, column=0, pady=(10, 10))
display_frame.grid_propagate(0)

keypad_frame = tk.LabelFrame(root_frame, width=400, height=530, bg="#1e1e1e")
keypad_frame.grid(row=1, column=0, padx=10, pady=(10,10))
keypad_frame.grid_propagate(0)

numbers_frame = tk.LabelFrame(keypad_frame, width=260, height=400, bg="#1e1e1e")
numbers_frame.grid(row=1, column=0, padx=(10, 20), pady=(20, 10))
numbers_frame.grid_propagate(0)

signs_frame = tk.LabelFrame(keypad_frame, width=100, height=400, bg="#1e1e1e")
signs_frame.grid(row=1, column=1, pady=(20, 10))
signs_frame.grid_propagate(0)

# Functions
def show(num):
    display_box.insert(tk.END, num)

def clear():
    display_box.delete("1.0", tk.END)

def assign(sign):
    global op, num1
    op = sign
    num1 = display_box.get("1.0", "end-1c")
    clear()

def calculate():
    global num2, op
    result = 0
    num2 = display_box.get("1.0", "end-1c")
    try:
        if op == "+":
            result = float(num1) + float(num2)
        elif op == "-":
            result = float(num1) - float(num2)
        elif op == "*":
            result = float(num1) * float(num2)
        elif op == "/":
            result = float(num1) / float(num2)
    except ZeroDivisionError:
        result = "Error"
    clear()
    display_box.insert(tk.END, result)

# Textbox
display_box = tk.Text(display_frame, width=20, height=1, font=("Helvetica", 30),
                      bg="#2c2c2c", fg="white", insertbackground="white")
display_box.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
window.bind("<BackSpace>", lambda event: backspace())

def backspace():
    current = display_box.get("1.0", "end-1c")
    if current:
        display_box.delete("1.0", tk.END)
        display_box.insert("1.0", current[:-1])

# Colors
btn_bg = "#3b3b3b"
btn_fg = "white"
btn_active = "#555555"

# Number Buttons 
button_1 = tk.Button(numbers_frame, text="1", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0, command=lambda: show("1"))
button_1.grid(row=0, column=0, padx=10, pady=14)

button_2 = tk.Button(numbers_frame, text="2", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("2"))
button_2.grid(row=0, column=1, padx=10, pady=14)

button_3 = tk.Button(numbers_frame, text="3", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("3"))
button_3.grid(row=0, column=2, padx=10, pady=14)

button_4 = tk.Button(numbers_frame, text="4", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("4"))
button_4.grid(row=1, column=0, padx=10, pady=14)

button_5 = tk.Button(numbers_frame, text="5", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("5"))
button_5.grid(row=1, column=1, padx=10, pady=14)

button_6 = tk.Button(numbers_frame, text="6", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("6"))
button_6.grid(row=1, column=2, padx=10, pady=14)

button_7 = tk.Button(numbers_frame, text="7", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("7"))
button_7.grid(row=2, column=0, padx=10, pady=14)

button_8 = tk.Button(numbers_frame, text="8", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("8"))
button_8.grid(row=2, column=1, padx=10, pady=14)

button_9 = tk.Button(numbers_frame, text="9", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("9"))
button_9.grid(row=2, column=2, padx=10, pady=14)

button_0 = tk.Button(numbers_frame, text="0", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("0"))
button_0.grid(row=3, column=0, padx=10, pady=14)

button_dot = tk.Button(numbers_frame, text=".", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=lambda: show("."))
button_dot.grid(row=3, column=1, padx=10, pady=14)

button_equals = tk.Button(numbers_frame, text="=", width=6, height=3, bg=btn_bg, fg=btn_fg,
activebackground=btn_active, relief="flat", bd=0, highlightthickness=0,command=calculate)
button_equals.grid(row=3, column=2, padx=10, pady=14)

button_clear = tk.Button(keypad_frame, text="CE", width=6, height=3,
bg="#ff9500", fg="white", activebackground="#e67e00",relief="flat", bd=0, highlightthickness=0, command=clear)
button_clear.grid(row=0, column=1, pady=(15, 4))

# Operator Buttons
button_add = tk.Button(signs_frame, text="+", width=6, height=3, command=lambda: assign("+"),
bg=btn_bg, fg=btn_fg, activebackground=btn_active, relief="flat", bd=0)
button_add.grid(row=0, column=0, padx=10, pady=14)

button_sub = tk.Button(signs_frame, text="-", width=6, height=3, command=lambda: assign("-"),
bg=btn_bg, fg=btn_fg, activebackground=btn_active, relief="flat", bd=0)
button_sub.grid(row=1, column=0, padx=10, pady=14)

button_mul = tk.Button(signs_frame, text="*", width=6, height=3, command=lambda: assign("*"),
bg=btn_bg, fg=btn_fg, activebackground=btn_active, relief="flat", bd=0)
button_mul.grid(row=2, column=0, padx=10, pady=14)

button_div = tk.Button(signs_frame, text="/", width=6, height=3, command=lambda: assign("/"),
bg=btn_bg, fg=btn_fg, activebackground=btn_active, relief="flat", bd=0)
button_div.grid(row=3, column=0, padx=10, pady=14)

# Font
btn_font = font.Font(size=12, weight="bold", family="Helvetica")

for btn in numbers_frame.winfo_children():
    btn["font"] = btn_font

for btn in signs_frame.winfo_children():
    btn["font"] = btn_font

button_clear["font"] = btn_font

window.mainloop()

