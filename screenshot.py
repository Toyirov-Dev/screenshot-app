import pyautogui
import time
from tkinter import*
from random import*


screen = Tk()
screen.title("screenshot")
screen.geometry('300x150')
screen.config(bg='#10497C')


# function
def screensh():
	time.sleep(6)
	s0 = Label(screen, text="Saqlandi!",
		fg='Black',
		font=('Times', 20, 'bold'),
		bg='#10497C')
	s0.place(x=100, y=60)

	img = pyautogui.screenshot()
	img.save(r"screen.png")

	print("screenshot muvofaqqiyatli saqlandi!")

# button
S_button = Button(screen, text='screenshot',
	bg='#1ECBE1',
	fg='black',
	font=('Times', 10, 'bold'),
	relief=SOLID,
	width=20,
	command=screensh)
S_button.place(x=75, y=20)

# Dasturchi:
Dasturchi = Label(screen, text=" created by Toyirov Ziyodullo! ",
	fg='Black',
	font=('Times', 10, 'italic'),
	bg='#19497C',
	relief=SOLID,
	bd=1)
Dasturchi.place(x=67, y=130)


screen.mainloop()