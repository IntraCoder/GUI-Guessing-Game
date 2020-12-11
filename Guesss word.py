from tkinter import *
from tkinter import messagebox as msg
import random

root = Tk()
root.geometry("500x300")
root.title("Intra Guessing Game")
root.config(bg="red")
root.resizable(width=False, height=False)

ran = RandomWords()


def show():
    new = ""
    for i in word:
        if i in pre_words:
            new += i
        else:
            new += "_ "
    return new


def finish():
    msg.showinfo("Won", "Guess was right!")
    lab.destroy()
    widgets()


def check():
    global chances, chance_lab,words

    entry = ent_var.get().lower()
    if len(entry) > 1 and len(entry) != len(word):
        msg.showerror("Invalid", "Please input only one char!")
        ent_var.set("")
    else:
        if entry == word:
            lab["text"] = word
            finish()
        else:
            if entry in word:
                pre_words.add(entry)
                lab["text"] = show()
                if lab["text"] == word:
                    finish()
            chances -= 1
            Label(root, text=f"Chance:{chances}",width=20, font="None 20", bg="red", fg="white").place(x=50, y=250)
            if chances == 0:
                msg.showerror("Lose", "You lost! Word ->" + word)
                lab.destroy()
                widgets()
    ent_var.set("")


def widgets():
    global chances, ent_var, word, pre_words, lab, chance_lab,words
    words = ["avengers","endgame","blue","dark","stranger things","hello","intra","peter","steve","dog"]
    pre_words = {"a", "e", "i", "o", "u", " "}

    word = random.choice(words)
    chances = len(word)
    
    Label(root, text=f"Chance:{chances}",width=20, font="None 20", bg="red", fg="white").place(x=50, y=250)
    lab = Label(root, text=show(), font="None 30", bg="red", fg="white")
    lab.place(x=100, y=50)

    ent_var = StringVar()
    Entry(root, font='None 17', textvariable=ent_var, relief=SUNKEN).place(x=140, y=130)
    Button(root, text="Check", font="None 20", height=1, width=10, bg="cyan", command=check).place(x=180,
                                                                                                   y=180)


widgets()

root.mainloop()
