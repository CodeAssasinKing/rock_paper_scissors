import tkinter as tk
import random

answers = ['stone', 'scissors', 'paper']
user_score = 0
computer_score = 0
def main():
    global root
    root = tk.Tk()
    root.geometry('1000x500')
    root.title('Game')

def users():
    lbl_user = tk.Label(root, text='User', font='TimesNewRoman, 20')
    lbl_user.grid(row=0, column=0, ipadx=120)

    lbl_comp = tk.Label(root, text='Computer', font='TimesNewRoman, 20')
    lbl_comp.grid(row=0, column=3, ipadx=120)

def users_scores():
    global lbl_user_score
    global lbl_comp_score
    lbl_user_score = tk.Label(root, text='0', font='TimesNewRoman, 20')
    lbl_user_score.grid(row=2, column=0, ipadx=120, ipady=20)

    lbl_comp_score = tk.Label(root, text='0', font='TimesNewRoman, 20')
    lbl_comp_score.grid(row=2, column=3, ipadx=120, ipady=20)


def users_answer():
    global lbl_user_answer
    global lbl_comp_answer
    lbl_user_answer = tk.Label(root, text='', font='TimesNewRoman, 20')
    lbl_user_answer.grid(row=3, column=0, ipadx=120, ipady=20)

    lbl_comp_answer = tk.Label(root, text='', font='TimesNewRoman, 20')
    lbl_comp_answer.grid(row=3, column=3, ipadx=120, ipady=20)


def update_label(lbl1, lbl2, lbl3, lbl4, lbl_draw, user_score, computer_score):
    user_choice = random.choice(answers)
    computer_choice = random.choice(answers)
    lbl1.config(text=user_choice)
    lbl2.config(text=computer_choice)
    lbl_draw.config(text='', background='white')
    if user_choice == 'stone' and computer_choice == 'scissors':
        user_score += 1
        lbl_draw.config(text='You win', background='green')
    elif user_choice == 'stone' and computer_choice == 'paper':
        computer_score += 1
        lbl_draw.config(text='Computer win', background='red')
    elif user_choice == 'stone' and computer_choice == 'stone':
        lbl_draw.config(text='Draw', background='yellow')
    elif user_choice == 'scissors' and computer_choice == 'stone':
        computer_score += 1
        lbl_draw.config(text='Computer win', background='red')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        user_score += 1
        lbl_draw.config(text='You win', background='green')
    elif user_choice == 'scissors' and computer_choice == 'scissors':
        lbl_draw.config(text='Draw', background='yellow')
    elif user_choice == 'paper' and computer_choice == 'stone':
        user_score += 1
        lbl_draw.config(text='You win', background='green')
    elif user_choice == 'paper' and computer_choice == 'scissors':
        computer_score += 1
        lbl_draw.config(text='Computer win', background='red')
    elif user_choice == 'paper' and computer_choice == 'paper':
        lbl_draw.config(text='Draw', background='yellow')
    lbl3.config(text=str(int(lbl3.cget('text')) + user_score))
    lbl4.config(text=str(int(lbl4.cget('text')) + computer_score))



def start(lbl1, lbl2, lbl3, lbl4, lbl_draw):
    update_label(lbl1, lbl2, lbl3, lbl4, lbl_draw, user_score, computer_score)

def button():
    global lbl_draw
    lbl_draw = tk.Label(root, text='', font='TimesNewRoman, 14', background='white')
    lbl_draw.grid(row=5, column=2, ipadx=100, ipady=20)
    start_button = tk.Button(root, text='Start', font='TimesNewRoman, 16', background='green', command=lambda: start(lbl_user_answer, lbl_comp_answer, lbl_user_score, lbl_comp_score, lbl_draw) , width=10)
    start_button.grid(row=4, column=2, ipadx=100)



main()
users()
users_scores()
users_answer()
button()
root.mainloop()