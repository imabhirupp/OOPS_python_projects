from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")                              # To make a dictionary with french and english word. Eg- [{"French": "Partie", "English": "Part"}, etc]

def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=fg_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card, image=bg_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def save_card():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# WINDOW

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# PHOTO-IMAGE

bg_image = PhotoImage(file="images/card_back.png")
fg_image = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# CANVAS

canvas = Canvas(width=800, height=526)
card = canvas.create_image(410, 268, image=fg_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "italic"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, rowspan=2, columnspan=2)

next_card()

# BUTTONS

wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(column=1, row=2)
wrong_button.config(highlightthickness=0)

right_button = Button(image=right_image, command=save_card)
right_button.grid(column=0, row=2)
right_button.config(highlightthickness=0)


window.mainloop()

