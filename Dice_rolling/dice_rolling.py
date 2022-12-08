import random
import time
from tkinter import *


def roll():
    x = random.choice(['b.png', 'b2.png', 'b3.png',
                       'b4.png', 'b5.png', 'b6.png'])
    return x


def img():
    global dice1, dice2
    for i in range(10):
        dice1 = PhotoImage(file=(roll()))
        dice2 = PhotoImage(file=(roll()))
        Lab1['image'] = dice1
        Lab2['image'] = dice2
        root.update()
        time.sleep(0.14)

root = Tk()
root.geometry('400x250')
root.title('dice_rolling!!!, Make roll of a dices!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='iconka.png'))
font = PhotoImage(file='holst.png')
Label(root, image=font).pack()
Lab1 = Label(root)
Lab1.place(relx=0.65, rely=0.35, anchor=CENTER)
Lab2 = Label(root)
Lab2.place(relx=0.35, rely=0.35, anchor=CENTER)
Button(root, text='Make a roll!', command=img).pack()
#root.bind('<1>', img())
img()


root.mainloop()
