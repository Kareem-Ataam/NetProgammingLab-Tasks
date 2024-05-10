from tkinter import *
from tkinter import messagebox
turn = 1
def clicked_1():
    global turn
    if btn_1["text"] == " ":
        if turn == 1:
            btn_1["text"] = "X"
            turn = 2
        else:
            btn_1["text"] = "O"
            turn = 1
    check()
def clicked_2():
    global turn
    if btn_2["text"] == " ":
        if turn == 1:
            btn_2["text"] = "X"
            turn = 2
        else:
            btn_2["text"] = "O"
            turn = 1
    check()
def clicked_3():
    global turn
    if btn_3["text"] == " ":
        if turn == 1:
            btn_3["text"] = "X"
            turn = 2
        else:
            btn_3["text"] = "O"
            turn = 1
    check()
def clicked_4():
    global turn
    if btn_4["text"] == " ":
        if turn == 1:
            btn_4["text"] = "X"
            turn = 2
        else:
            btn_4["text"] = "O"
            turn = 1
    check()
def clicked_5():
    global turn
    if btn_5["text"] == " ":
        if turn == 1:
            btn_5["text"] = "X"
            turn = 2
        else:
            btn_5["text"] = "O"
            turn = 1
    check()
def clicked_6():
    global turn
    if btn_6["text"] == " ":
        if turn == 1:
            btn_6["text"] = "X"
            turn = 2
        else:
            btn_6["text"] = "O"
            turn = 1
    check()
def clicked_7():
    global turn
    if btn_7["text"] == " ":
        if turn == 1:
            btn_7["text"] = "X"
            turn = 2
        else:
            btn_7["text"] = "O"
            turn = 1
    check()
def clicked_8():
    global turn
    if btn_8["text"] == " ":
        if turn == 1:
            btn_8["text"] = "X"
            turn = 2
        else:
            btn_8["text"] = "O"
            turn = 1
    check()
def clicked_9():
    global turn
    if btn_9["text"] == " ":
        if turn == 1:
            btn_9["text"] = "X"
            turn = 2
        else:
            btn_9["text"] = "O"
            turn = 1
    check()
flag =  1
def check():
    global flag
    flag += 1
    if btn_1["text"] == btn_2["text"] == btn_3["text"] != " ":
        win (btn_1["text"])
    elif btn_4["text"] == btn_5["text"] == btn_6["text"] != " ":
        win (btn_4["text"])
    elif btn_7["text"] == btn_8["text"] == btn_9["text"] != " ":
        win (btn_7["text"])
    elif btn_1["text"] == btn_5["text"] == btn_9["text"] != " ":
        win (btn_1["text"])
    elif btn_3["text"] == btn_5["text"] == btn_7["text"] != " ":
        win (btn_3["text"])
    elif btn_1["text"] == btn_4["text"] == btn_7["text"] != " ":
        win (btn_1["text"])
    elif btn_2["text"] == btn_5["text"] == btn_8["text"] != " ":
        win (btn_2["text"])
    elif btn_3["text"] == btn_6["text"] == btn_9["text"] != " ":
        win (btn_3["text"])
    if flag == 10:
        messagebox.showinfo("Dead Game","Game Over!! Try again")
        window.destroy()

def win(button_text):
    if button_text == "X":
        messagebox.showinfo("Congratulations","Player 1 Wins")
        window.destroy()
    else:
        messagebox.showinfo("Congratulations", "Player 2 Wins")
        window.destroy()
def reset_game():
    btn_1["text"] = btn_2["text"]  = btn_3["text"]  = btn_4["text"]  = \
        btn_5["text"]  = btn_6["text"]  = btn_7["text"]  = btn_8["text"]  = btn_9["text"]  = " "
    global turn 
    global flag
    turn = 1
    flag = 1
window = Tk()


# Window setup
window.title("Tic-Tac-Toe")
window.geometry("400x300")

title_label = Label(window, text="Tic-tac-toe Game",font=("Tahoma", "15"))
title_label.grid(row=0, column=0)

player_1_label = Label(window, text="Player 1 : X", font=("Tahoma", "10"))
player_1_label.grid(row=1, column=0)
player_2_label = Label(window, text="Player 2 : O", font=("Tahoma", "10"))
player_2_label.grid(row=2, column=0)





# List of buttons

btn_1 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_1)
btn_1.grid(row=1, column=1)
btn_2 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_2)
btn_2.grid(row=1, column=2)
btn_3 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_3)
btn_3.grid(row=1, column=3)
btn_4 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_4)
btn_4.grid(row=2, column=1)
btn_5 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_5)
btn_5.grid(row=2, column=2)
btn_6 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_6)
btn_6.grid(row=2, column=3)
btn_7 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_7)
btn_7.grid(row=3, column=1)
btn_8 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_8)
btn_8.grid(row=3, column=2)
btn_9 = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=("Tahoma", "20"), command=clicked_9)
btn_9.grid(row=3, column=3)

reset_btn_frame = Frame(window)
reset_btn_frame.grid(row=5, column=1 )
button_style = {'font': ('Helvetica', 12), 'width': 5, 'height': 2}

reset_btn = Button(window, text="Reset", bg="red", fg="white", **button_style, command=reset_game)
reset_btn.grid(row=5, column=2)







window.mainloop()