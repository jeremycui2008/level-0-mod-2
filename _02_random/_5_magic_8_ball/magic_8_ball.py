import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    ball_of_wisdom = 0
    # Make a variable and initialize it to a random number between 0 and 3
    ball_of_wisdom=random.randint(0,3)
    # If the random number is 0
    if ball_of_wisdom==0:
        messagebox.showinfo(title='yes', message='yes')
        # tell the user "Yes"

    # If the random number is 1
    elif ball_of_wisdom==1:
        messagebox.showinfo(title='no', message='no')
        # tell the user "No"

    # If the random number is 2
    elif ball_of_wisdom==2:
        messagebox.showinfo(title='Google', message='Maybe you should ask Google?')
        # tell the user "Maybe you should ask Google?"
    elif ball_of_wisdom==3:
        messagebox.showinfo(title='Maybe', message='Maybe')
    # If the random number is 3

        # write your own answer
