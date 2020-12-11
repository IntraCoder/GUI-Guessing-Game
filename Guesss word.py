from tkinter import *
from tkinter import messagebox as msg
import random


def game():
    root = Tk()
    root.geometry("670x440")
    root.title("Intra Guessing Game")
    root.config(bg="red")
    root.resizable(width=False, height=False)
    head = PhotoImage(file="guess_head.png")

    def show():
        new = ""
        for i in word:
            if i in pre_words:
                new += i
            else:
                new += "_ "
        return new

    def finish():
        confirm = msg.askyesno("Won", "Guess was right!\nWant to play again?")
        if confirm:
            root.destroy()
            game()
        else:
            root.destroy()

    def check():
        global chances, chance_lab, words, word

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
                Label(root, text=f"Chance:{chances}", width=20, font="None 20", bg="red", fg="white").place(x=60, y=350)
                if chances == 0:
                    msg.showerror("Lose", "You lost! Word ->" + word)
                    finish()

        ent_var.set("")

    global word, chances
    words = ["avengers", "endgame", "blue", "dark", "stranger  things", "hello", "intra", "peter", "steve", "dog"]
    pre_words = {"a", "e", "i", "o", "u", " "}
    word = random.choice(words)
    chances = len(word)

    Label(root, image=head, bg="red").pack()
    Label(root, text=f"Chance:{chances}", width=20, font=(None, 20, "bold"), bg="red", fg="white").place(x=60, y=350)
    lab = Label(root, text=show(), font="None 30", bg="red", fg="white")
    lab.pack()

    ent_var = StringVar()
    Entry(root, font='None 20', textvariable=ent_var, relief=SUNKEN).pack(pady=10)
    Button(root, text="Check", font="None 20", height=1, width=10, bg="cyan", command=check).pack(pady=10)

    root.mainloop()


game()
