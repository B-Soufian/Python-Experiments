from tkinter import *
import random

def next_turn(button, row, column):
    global player

    if button["text"] == "" and check_winner() is False:
        button["text"] = player

        if check_winner() is False:
            if player == players[0] :
                player = players[1] 
            else :
                player =  players[0]

            label.config(text=player + " turn")

        elif check_winner() is True:
            label.config(text=player + " wins")

        elif check_winner() == "Tie":
            label.config(text="Tie!")

def ran():
    butoons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for i in  butoons :
        botch = random.choice(butoons)
        if botch['text'] == "" :
            return True
        else :
            return False

def check_winner():
    if (b1["text"] == b2["text"] == b3["text"] != "" or  
        b4["text"] == b5["text"] == b6["text"] != "" or  
        b7["text"] == b8["text"] == b9["text"] != "" or

        b1["text"] == b4["text"] == b7["text"] != "" or  
        b2["text"] == b5["text"] == b8["text"] != "" or  
        b3["text"] == b6["text"] == b9["text"] != "" or

        b1["text"] == b5["text"] == b9["text"] != "" or  
        b3["text"] == b5["text"] == b7["text"] != "" ):  

        return True

    if empty_spaces() is False:
        return "Tie"
    
    else : 
        return False

def empty_spaces():
    spa = 0
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        if button["text"] != "" :
            spa += 1
    if spa == 9 :
        return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        button["text"] = "" 
window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = Label(window, text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(window, text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

b1 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b1, 0, 0))
b1.grid(row=0, column=0)

b2 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b2, 0, 1))
b2.grid(row=0, column=1)

b3 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b3, 0, 2))
b3.grid(row=0, column=2)

b4 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b4, 1, 0))
b4.grid(row=1, column=0)

b5 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b5, 1, 1))
b5.grid(row=1, column=1)

b6 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b6, 1, 2))
b6.grid(row=1, column=2)

b7 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b7, 2, 0))
b7.grid(row=2, column=0)

b8 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b8, 2, 1))
b8.grid(row=2, column=1)

b9 = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda: next_turn(b9, 2, 2))
b9.grid(row=2, column=2)

empty_spaces()
print(ran())
window.mainloop()

