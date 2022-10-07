
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/vietnamese_words.csv")
finally:
    words_list = data.to_dict(orient="records")


used_indexes = []
card = None


def draw_card():
    global card, flipping
    window.after_cancel(flipping)
    card = random.choice(words_list)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_language, text="Vietnamese", fill="black")
    canvas.itemconfig(card_word, text=card["Vietnamese"], fill="black")
    flipping = window.after(4000, flip)


def flip():
    global flipping
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")


def known_word():
    words_list.remove(card)
    data = pandas.DataFrame(words_list)
    data.to_csv("./data/words_to_learn.csv", index=False)
    draw_card()


window = Tk()
window.title("Blizy Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipping = window.after(4000, flip)

# images
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
tick_button_img = PhotoImage(file="./images/tick.png")
x_button_img = PhotoImage(file="./images/x.png")

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, )
card_language = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, rowspan=2, columnspan=2)

tick_button = Button(image=tick_button_img,
                     highlightthickness=0, command=known_word)
tick_button.grid(column=1, row=3)

x_button = Button(image=x_button_img, highlightthickness=0,
                  command=draw_card)
x_button.grid(column=0, row=3)

draw_card()
window.mainloop()
