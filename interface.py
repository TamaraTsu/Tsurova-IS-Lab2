
from textwrap import fill
from tkinter import *


window = Tk()
window.title('PROGRAM')
window.geometry("500x300")


frame = LabelFrame(window, width=200, height=200, bg="skyblue3")
frame.grid(row=0,column=0)
frame.propagate(0)

label1 = Label(frame, text='The Best Genes:',
               background="skyblue3").pack(side=TOP, anchor="w")
label2 = Label(frame, text='To be or not to be',
               background="skyblue3").pack(pady=(0,10),side=TOP, anchor="w")

label3 = Label(frame, text='Generation' +
               ' #35',
               background="skyblue3").pack(side=TOP, anchor="w")

label4 = Label(frame, text='Total Population' +
               ' 600',
               background="skyblue3").pack(side=TOP, anchor="w")

label5 = Label(frame, text='Average fitness :' +
               '67.89%',
               background="skyblue3").pack(side=TOP, anchor="w")

label6 = Label(frame, text='Max fitness :' +
               '100%',
               background="skyblue3").pack(side=TOP, anchor="w")

label7 = Label(frame, text='M... rate :' +
               '2.0%',
               background="skyblue3").pack(side=TOP, anchor="w")

frame2 = LabelFrame(window, width=300, height=200, bg="skyblue2")
frame2.grid(row=0,column=1)
frame2.propagate(0)

scrollbar = Scrollbar(frame2,orient=VERTICAL)

listbox = Listbox(frame2,yscrollcommand= scrollbar.set,width=290)
scrollbar.config(command= listbox.yview)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.pack(side=LEFT,fill=BOTH)
for values in range(100):
    listbox.insert(END, values)

window.mainloop()
