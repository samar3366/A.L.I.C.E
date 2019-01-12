from tkinter import *

win = Tk()

win.geometry('500x400')
win.title("cwd - A.L.I.C.E")
win.resizable(0, 0)

menu = Menu(win)

win.config(Menu = menu)

pathsmenu = Menu(menu)
menu.add_cascade(label = 'File', menu = pathsmenu)
pathsmenu.add_command(label = 'New')
pathsmenu.add_command(label = 'Open')

win.mainloop()
