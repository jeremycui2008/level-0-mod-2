import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    x=0
    y=""
    for i in range(6):
        x=random.randint(1,60)
        y+=" "+str(x)
    messagebox.showinfo(title='lottery ticket', message=y)
    # TODO 1) Get 6 random numbers to put on your lottery ticket

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
