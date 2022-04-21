from cgitb import text
from tkinter import *


class App:
    def add_list(self):
        for values in range(100):
            self.listbox.insert(END, values)

    def __init__(self):
        self.window = Tk()
        self.window.title("Genetic Algorithm")
        self.window.geometry("600x350")
        self.window.resizable(False, False)
        self.window.iconbitmap("geneicon.ico")

        # Left frame for information
        self.frame = LabelFrame(self.window, width=300,
                                height=250, bg="#465B75", bd=1, relief=FLAT)
        self.frame.place(x=0, y=0)
        self.frame.propagate(0)

        # All labels
        self.label1 = Label(self.frame, text='The Best Genes:', font=20,
                            background="#465B75")
        self.label1.pack(side=TOP, anchor="w")

        self.label2 = Label(self.frame, text='To be or not to be', font=20,
                            background="#465B75")
        self.label2.pack(pady=(0, 10), side=TOP, anchor="w")

        self.label3 = Label(self.frame, text='Generation' +
                            ' #35', font=20,
                            background="#465B75")
        self.label3.pack(side=TOP, anchor="w")

        self.label4 = Label(self.frame, text='Total Population :' +
                            ' ', font=20,
                            background="#465B75")
        self.label4.pack(side=TOP, anchor="w")

        self.label5 = Label(self.frame, text='Average fitness :' +
                            '67.89%', font=20,
                            background="#465B75")
        self.label5.pack(side=TOP, anchor="w")

        self.label6 = Label(self.frame, text='Max fitness :' +
                            '100%', font=20,
                            background="#465B75")
        self.label6.pack(side=TOP, anchor="w")

        self.label7 = Label(self.frame, text='Mutation rate :' +
                            ' ', font=20,
                            background="#465B75")
        self.label7.pack(side=TOP, anchor="w")

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)

        # Right frame for list box
        self.frame2 = LabelFrame(
            self.window, width=300, height=250, bg="#465B75", bd=1, relief=FLAT)
        self.frame2.place(x=300, y=0)
        self.frame2.propagate(0)

        self.scrollbar = Scrollbar(self.frame2, orient=VERTICAL)

        self.listbox = Listbox(
            self.frame2, yscrollcommand=self.scrollbar.set, width=290)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox.pack(side=LEFT, fill=BOTH)

        # Bottom Input
        self.frame3 = LabelFrame(
            self.window, width=600, height=100, bg="#465B75", bd=1, relief=FLAT,)
        self.frame3.grid(pady=(250, 0))
        self.frame3.grid_propagate(False)

        self.labelpopul = Label(self.frame3, text='Population:', font=19,
                                background="#465B75")
        self.labelpopul.grid(column=0, row=0)
        self.inputpopul = Entry(self.frame3, width=23)
        self.inputpopul.grid(column=1, row=0)


        self.labeltarget = Label(self.frame3, text='Target:', font=19,
                                 background="#465B75")
        self.labeltarget.grid(column=0, row=1)

        self.inputtarget = Entry(self.frame3, width=23)
        self.inputtarget.grid(column=1, row=1)

        self.labelpoprate = Label(self.frame3, text='Mutation Rate:', font=19,
                                  background="#465B75")
        self.labelpoprate.grid(column=0, row=2)
        self.inputpoprate = Entry(self.frame3, width=23)
        self.inputpoprate.grid(column=1, row=2)
    
        def click():
            self.label4['text']='Total Population : ' + self.inputpopul.get()
            self.label7['text']='Mutation rate : ' + self.inputpoprate.get() +'%'
                            

        self.buttongo = Button(self.frame3, text='GO!', height=2, width=10,
                               activebackground='#345', activeforeground='white',command=click).grid(column=3, row=1, padx=(110))


        self.window.mainloop()


app = App()
