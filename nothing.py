from tkinter import *


def handler1(event):
    return print('hello again')


root = Tk()


hello_label = Label(root, text="hello world!", font='Times 40')
hello_label.pack()
print(hello_label.bind('<Button-1>', handler1))
root.mainloop()
