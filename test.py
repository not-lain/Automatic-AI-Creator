
from tkinter import filedialog
from tkinter import *

filename = ''


def input_function():
    global filename
    global var
    filename = filedialog.askdirectory()
    text.set(f"folder : {filename} ")


def extraction():
    global filename
    print(filename)


window = Tk()
window.geometry("860x500")


btn = Button(text="Input", command=input_function).pack()


text = StringVar()
text.set("click on input ! ")
label = Label(window, textvariable=text).pack()


btn2 = Button(window, text="Build", command=extraction).pack()

text2 = StringVar()
text2.set("model trained successfully")
text3 = StringVar()
text3.set("accuracy 94%")
text4 = StringVar()
text4.set("model saved !")
label2 = Label(window, textvariable=text2).pack()
label3 = Label(window, textvariable=text3).pack()
label4 = Label(window, textvariable=text4).pack()

btn2 = Button(window, text="Host The AI", command=extraction).pack()

window.mainloop()
